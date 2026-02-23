import json
from langchain_groq import ChatGroq
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from retrieval.vectorstore import load_vectorstore
from memory.session_memory import load_memory, save_memory
from core.prompt import mentor_prompt
from tools.tools import export_pitch_pdf


class PitchEngine:

    def __init__(self):

        self.llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            temperature=0.4,
        ).bind_tools([export_pitch_pdf])

        self.vectorstore = load_vectorstore()
        self.retriever = self.vectorstore.as_retriever(search_kwargs={"k": 4})

        self.chain = (
            {
                "memory": lambda x: json.dumps(load_memory(), indent=2),
                "context": self.retriever,
                "input": RunnablePassthrough(),
            }
            | mentor_prompt
            | self.llm
        )

    def evaluate_pitch(self, user_input):

        result = self.chain.invoke(user_input)

        if hasattr(result, "tool_calls") and result.tool_calls:
            tool_call = result.tool_calls[0]
            tool_result = export_pitch_pdf.invoke(tool_call["args"])
            return {"mentor_response": tool_result}

        try:
            parsed = json.loads(result.content)
        except:
            return {"mentor_response": "Invalid JSON returned from model."}

        memory = load_memory()
        new_memory = parsed.get("memory_update", {})

        updated_memory = memory.copy()
        for key in updated_memory.keys():
            if key in new_memory and new_memory[key]:
                updated_memory[key] = new_memory[key]

        save_memory(updated_memory)

        return parsed
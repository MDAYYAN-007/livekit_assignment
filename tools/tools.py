from langchain.tools import tool
from tools.pdf_generator import generate_pitch_pdf


@tool
def export_pitch_pdf(content: str) -> str:
    """
    Generates a downloadable PDF using the provided content.
    The content should already be structured and formatted by the LLM.
    """

    data = {
        "PitchSense Report": content
    }

    filename = generate_pitch_pdf(data)

    return f"PDF generated successfully: {filename}"
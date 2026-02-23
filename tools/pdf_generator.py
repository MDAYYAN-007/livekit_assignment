from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet

def generate_pitch_pdf(data: dict, filename: str = "pitch_report.pdf"):

    doc = SimpleDocTemplate(filename)
    elements = []
    styles = getSampleStyleSheet()

    elements.append(Paragraph("PitchSense Report", styles["Heading1"]))
    elements.append(Spacer(1, 0.3 * inch))

    for key, value in data.items():
        elements.append(Paragraph(f"<b>{key}</b>", styles["Heading2"]))
        elements.append(Spacer(1, 0.1 * inch))

        if isinstance(value, list):
            for item in value:
                elements.append(Paragraph(f"- {item}", styles["Normal"]))
        else:
            elements.append(Paragraph(str(value), styles["Normal"]))

        elements.append(Spacer(1, 0.2 * inch))

    doc.build(elements)

    return filename
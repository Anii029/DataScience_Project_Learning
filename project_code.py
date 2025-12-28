import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(csv_file):
    df = pd.read_csv(csv_file)
    subjects = df["Subject"]
    scores = df["Score"]

    today = datetime.now().strftime("%B-%Y")
    pdf_name = f"Student_Performance_Report_{today}.pdf"

    plt.bar(subjects, scores)
    plt.savefig("chart.png")
    plt.close()

    doc = SimpleDocTemplate(pdf_name, pagesize=A4)
    styles = getSampleStyleSheet()

    table_data = [["Subject", "Score"]] + df.values.tolist()
    table = Table(table_data)
    table.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 1, colors.black)
    ]))

    doc.build([Paragraph("Student Performance Report", styles["Title"]), Spacer(1,20), table])

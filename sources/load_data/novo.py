"""Generate Reports With for Analisys"""

import os
from typing import Type, Tuple

import pandas as pd
from pandas import DataFrame
import numpy as np
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Frame, Table, Spacer, TableStyle
from reportlab.lib.enums import TA_CENTER


class ReportGenerator:
    """Class to Generate Reports"""

    def __init__(self, name:str, dates: Tuple[str, str], 
        content: Type[DataFrame], directory: str) -> None:
        """Render Pdf with Content Informations"""
        self.story = []
        
        """Define Components"""
        self.set_title()
        self.set_table(content)
        self.story.append(Spacer(1, 20))

        
        c = Canvas(os.path.join(directory, name+'.pdf'))
        f = Frame(inch, inch, 6 * inch, 9 * inch)
        f.addFromList(self.story, c)
        c.save()

    def set_title(self) -> None:
        """Set a Documento Title"""
        self.story.append(
            Paragraph(
                "Fatura Semanal - G4 MOBILE", 
                ParagraphStyle('yourtitle',
                           fontName="Courier",
                           fontSize=16,
                           parent=getSampleStyleSheet()['Heading2'],
                           alignment=1,
                           spaceAfter=35)))

    def set_table(self, content) -> None:
        """Format and Insert Table in Story"""
        df = content.reset_index()
        df = df.rename(columns={"index": ""})
        data = [df.columns.to_list()] + df.values.tolist()
        table = Table(data).setStyle(
            TableStyle(
                [
                    ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                    ('BOX', (0, 0), (-1, -1), 0.25, colors.black)
                ]
            ))
        self.story.append(table)
        

        

if __name__ == '__main__':
    from context import motorista
    ReportGenerator("mariano", ("10-10-10", "10-10-10"), motorista, './')
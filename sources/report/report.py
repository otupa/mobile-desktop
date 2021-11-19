"""Generate Reports With for Analisys"""

import os
from typing import Type, Tuple

from pandas import DataFrame
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
        self.set_infos(name, dates)
        self.set_table(content)
        self.story.append(Spacer(1, 20))

        """Save Pdf"""
        canvas_ = Canvas(os.path.join(directory, name+'.pdf'))
        frame_ = Frame(inch, inch, 6 * inch, 9 * inch)
        frame_.addFromList(self.story, canvas_)
        canvas_.save()

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

    def set_infos(self, name, dates) -> None:
        """Set a Documento Infos"""
        self.story.append(
            Paragraph(
                "{} {} - {}".format(name, *dates), 
                ParagraphStyle('yourtitle',
                           fontName="Courier",
                           fontSize=12,
                        #    parent=getSampleStyleSheet()['Heading6'],
                           alignment=1,
                           spaceAfter=20)))

    def set_table(self, content) -> None:
        """Format and Insert Table in Story"""
        data_frame = content.reset_index()
        data_frame = data_frame.rename(columns={"index": ""})
        data = [data_frame.columns.to_list()] + data_frame.values.tolist()
        table = Table(data)
        table.setStyle(
            TableStyle([
                ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                ('BOX', (0, 0), (-1, -1), 0.25, colors.black)]))
        self.story.append(table)

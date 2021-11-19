"""Generate Reports With for Analisys"""

from context import motorista

from reportlab.pdfgen import canvas
from reportlab.platypus import *
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
import pandas as pd
import numpy as np


class ReportGenerator:
    """Class to Generate Reports"""

    def __init__(self) -> None:
        pass


import pandas as pd
import numpy as np
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Frame, Table, Spacer, TableStyle

# Sample DataFrame
df = pd.DataFrame(np.random.randn(5, 4), columns=['one', 'two', 'three', 'four'],
                  index=['a', 'b', 'c', 'd', 'e'])

# Style Table
df = df.reset_index()
df = df.rename(columns={"index": ""})
data = [df.columns.to_list()] + df.values.tolist()
table = Table(data)
table.setStyle(TableStyle([
    ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
    ('BOX', (0, 0), (-1, -1), 0.25, colors.black)
]))

# Components that will be passed into a Frame
story = [Paragraph("My Report", getSampleStyleSheet()['Heading1']),
         Spacer(1, 20),
         table]

# Use a Frame to dynamically align the compents and write the PDF file
c = Canvas('report.pdf')
f = Frame(inch, inch, 6 * inch, 9 * inch)
f.addFromList(story, c)
c.save()

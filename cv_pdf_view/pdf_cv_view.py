from io import BytesIO
from cv_pdf_view.models import PersonalInfo, Study, Job, SocialMedia, Language, HardSkill, SoftSkill

from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Table, TableStyle, HRFlowable
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))

PAGESIZE = letter
BASE_MARGIN = 5 * mm

table_style = TableStyle([
    ('LINEABOVE', (0, 0), (-1, 0), 2, '#D1C7FF'),
    ('LINEBELOW', (0, -1), (-1, -1), 2, '#D1C7FF'),
    ('VALIGN', (0, 0), (-1, -1), 'BOTTOM'),
    ('INNERGRID', (0, 0), (-1, -1), 0.25, '#ffffff'),
    ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
    ('LINEAFTER', (0, 0), (-1, -1), 0.25, colors.black),
    ('FONTNAME', (0, 0), (0, -1), 'VeraBd'),
    ('FONTNAME', (1, 0), (1, -1), 'VeraBd'),
])

styles = getSampleStyleSheet()
styleH = styles['Heading1']
styleH2 = styles['Heading2']


class PdfCreatorPort:
    def header_footer(self, canvas, doc):
        canvas.saveState()

        # header image --------------------------------------

        header_image = Image('media/images/5.png', doc.width, 60)

        w, h = header_image.wrap(doc.width, doc.topMargin)

        header_image.drawOn(canvas, (doc.leftMargin),
                            doc.height + doc.topMargin - 0.85*h)

        # ----------------------------------------------------

        # my info -------------------------------------------

        my_info = PersonalInfo.objects.all()
        for row in my_info:
            name = str(row.name)
            position = str(row.position)
            address = str(row.address)
            phone = str(row.phone)
            linkedin = str(row.linkedin)

        # name ----------------------------------------------
        header_text1_style = ParagraphStyle('My Para style',
                                            fontSize=16,
                                            fontName='VeraBd',
                                            )

        header_text1 = Paragraph(name, header_text1_style)

        w, h = header_text1.wrap(doc.width, doc.bottomMargin)

        header_text1.drawOn(canvas,   0.4*w - doc.leftMargin,
                            doc.height + doc.topMargin - 1.5*h)

        # ----------------------------------------------------

        # position ------------------------------------------

        header_text2_style = ParagraphStyle('My Para style',
                                            fontSize=12,
                                            fontName='Vera',
                                            )

        header_text2 = Paragraph(position, header_text2_style)

        w, h = header_text2.wrap(doc.width, doc.bottomMargin)

        header_text2.drawOn(canvas, 0.53*w - doc.leftMargin,
                            doc.height + doc.topMargin - 3.3*h)

        # ----------------------------------------------------

        # phone ---------------------------------------------

        header_text3_style = ParagraphStyle('My Para style',
                                            fontSize=10,
                                            fontName='Vera',
                                            )

        phone = f"Cel: {phone}"

        header_text3 = Paragraph(phone, header_text3_style)

        w, h = header_text3.wrap(doc.width, doc.bottomMargin)

        header_text3.drawOn(canvas, doc.leftMargin,
                            doc.height + doc.topMargin - 5.3*h)

        # ----------------------------------------------------

        # linkedin -------------------------------------------

        header_text4_style = ParagraphStyle('My Para style',
                                            fontSize=10,
                                            fontName='Vera',
                                            )

        header_text4 = Paragraph(linkedin, header_text4_style)

        w, h = header_text4.wrap(doc.width, doc.bottomMargin)

        header_text4.drawOn(canvas, doc.leftMargin + 0.3*w,
                            doc.height + doc.topMargin - 5.3*h)

        # ----------------------------------------------------

        # address -------------------------------------------

        header_text5_style = ParagraphStyle('My Para style',
                                            fontSize=10,
                                            fontName='Vera',
                                            )

        header_text5 = Paragraph(address, header_text5_style)

        w, h = header_text5.wrap(doc.width, doc.bottomMargin)

        header_text5.drawOn(canvas, doc.leftMargin + 0.805*w,
                            doc.height + doc.topMargin - 5.3*h)

        # ----------------------------------------------------

        # hr ------------------------------------------------
        canvas.setStrokeColorRGB(0.824, 0.78, 1)

        canvas.line(doc.leftMargin, doc.height + doc.topMargin -
                    5.65*h, doc.leftMargin + w, doc.height + doc.topMargin - 5.65*h)

        # ----------------------------------------------------

        # hr for footer --------------------------------------
        canvas.setStrokeColorRGB(0.824, 0.78, 1)

        canvas.line(doc.leftMargin, 2*h, doc.leftMargin + w, 2*h)

        # ----------------------------------------------------

        # footer -------------------------------------------

        footer_style = ParagraphStyle('My Para style',
                                            fontSize=8,
                                            fontName='Vera',
                                            )

        footer = Paragraph(
            'PDF created using CV Creator. https://github.com/cathesposito/cv_creator :)', footer_style)

        w, h = footer.wrap(doc.width, doc.bottomMargin)

        footer.drawOn(canvas, doc.leftMargin, 0.5*h)

        # ----------------------------------------------------

        canvas.setTitle("CV Creator")

        canvas.restoreState()

    def get_body_style(self):
        sample_style_sheet = getSampleStyleSheet()
        body_style = sample_style_sheet['BodyText']
        body_style.spaceAfter = 5*mm
        body_style.wordWrap = 'CJK'
        body_style.fontName = 'Vera'
        body_style.fontSize = 10

        return body_style

    def get_heading1_style(self):
        sample_style_sheet = getSampleStyleSheet()
        heading1_style = sample_style_sheet['Heading1']
        heading1_style.spaceAfter = 5*mm

        return heading1_style

    def get_heading2_style(self):
        sample_style_sheet = getSampleStyleSheet()
        heading2_style = sample_style_sheet['Heading2']
        heading2_style.spaceAfter = 3*mm

        return heading2_style

    def get_bullet_style(self):
        sample_style_sheet = getSampleStyleSheet()
        bullet_style = sample_style_sheet['Normal']
        bullet_style.bulletColor = '#D1C7FF'
        bullet_style.bulletText = '-'
        bullet_style.spaceAfter = 5*mm

        return bullet_style

    def build_pdf(self):

        pdf_buffer = BytesIO()

        my_doc = SimpleDocTemplate(
            pdf_buffer,
            pagesize=PAGESIZE,
            topMargin=BASE_MARGIN*6,
            leftMargin=BASE_MARGIN,
            rightMargin=BASE_MARGIN,
            bottomMargin=BASE_MARGIN,
        )

        heading1_style = self.get_heading1_style()

        heading2_style = self.get_heading2_style()

        body_style = self.get_body_style()

        bullet_style = self.get_bullet_style()

        flowables = []

        # Resume Objective ----------------------------------------------------

        flowables.append(Paragraph("Resume Objective", heading1_style))

        paragraph_1 = PersonalInfo.objects.values_list(
            'resume_objective', flat=True).first()


        flowables.append(Paragraph(paragraph_1, body_style))

        flowables.append(HRFlowable(width='100%', thickness=2, color='#D1C7FF', spaceAfter=10,
                                    vAlign='MIDDLE', lineCap='round'))

        # ---------------------------------------------------------------------

        # Skills --------------------------------------------------------------

        flowables.append(Paragraph("Skills", heading1_style))

        table_skills = list(
            HardSkill.objects.values_list('skill', flat=True).all())

        table_skills = [[el] for el in table_skills]

        table_skills_wid = (10*mm*mm, 26*mm*mm)

        for i, item in enumerate(SoftSkill.objects.all()):

            # Inputs Table

            table_skills[i].append(item.skill)

        flowables.append(Table(table_skills, style=table_style,
                               colWidths=table_skills_wid, hAlign='CENTER', spaceAfter=10))

        flowables.append(HRFlowable(width='100%', thickness=2, color='#D1C7FF', spaceAfter=10,
                                    vAlign='MIDDLE', lineCap='round'))

        # ---------------------------------------------------------------------

        # Work experience -----------------------------------------------------

        flowables.append(Paragraph("Work experience", heading1_style))

        get_works = Job.objects.order_by('-end').all()

        for i, item in enumerate(get_works):

            # Inputs Table
            flowables.append(Paragraph(item.title, heading2_style))
            flowables.append(Paragraph(item.location, body_style))
            if item.current is True:
                flowables.append(
                    Paragraph(f"{item.start}—Current", body_style))
            else:
                flowables.append(
                    Paragraph(f"{item.start}—{item.end}", body_style))
            flowables.append(Paragraph(item.description, body_style))
            flowables.append(
                Paragraph(f"Soft Skills: {item.soft_skills}", body_style))
            flowables.append(
                Paragraph(f"Hard Skills: {item.hard_skills}", body_style))
            if i != (len(get_works)-1):
                flowables.append(HRFlowable(width='100%', thickness=2, color='#D1C7FF', spaceAfter=2,
                                            vAlign='MIDDLE', lineCap='square', dash=(1, 4)))
            else:
                flowables.append(HRFlowable(width='100%', thickness=2, color='#D1C7FF', spaceAfter=10,
                                            vAlign='MIDDLE', lineCap='round'))

        # ---------------------------------------------------------------------

        # Education Objective -------------------------------------------------

        flowables.append(Paragraph("Education", heading1_style))

        get_studies = Study.objects.order_by('-end').all()

        for i, item in enumerate(get_studies):

            # Inputs Table
            flowables.append(Paragraph(item.title, heading2_style))
            flowables.append(Paragraph(item.location, body_style))
            if item.current is True:
                flowables.append(
                    Paragraph(f"{item.start}—Current", body_style))
            else:
                flowables.append(
                    Paragraph(f"{item.start}—{item.end}", body_style))
            flowables.append(Paragraph(item.description, body_style))
            if item.description2 != "":
                flowables.append(Paragraph(item.description2, body_style))
            flowables.append(Paragraph(f"Skills: {item.skills}", body_style))
            if i != (len(get_studies)-1):
                flowables.append(HRFlowable(width='100%', thickness=2, color='#D1C7FF', spaceAfter=2,
                                            vAlign='MIDDLE', lineCap='square', dash=(1, 4)))
            else:
                flowables.append(HRFlowable(width='100%', thickness=2, color='#D1C7FF', spaceAfter=10,
                                            vAlign='MIDDLE', lineCap='round'))

        # ---------------------------------------------------------------------

        # Social Medias -------------------------------------------------------

        flowables.append(Paragraph("Social Medias", heading2_style))

        get_medias = SocialMedia.objects.all()

        for i, item in enumerate(get_medias):

            # Inputs Table
            flowables.append(Paragraph(item.path, bullet_style))

        flowables.append(HRFlowable(width='100%', thickness=2, color='#D1C7FF', spaceAfter=10,
                                    vAlign='MIDDLE', lineCap='round'))

        # ---------------------------------------------------------------------

        # Languages -----------------------------------------------------------

        flowables.append(Paragraph("Languages", heading2_style))

        get_languages = Language.objects.all()

        for i, item in enumerate(get_languages):

            # Inputs Table
            flowables.append(Paragraph(item.language, bullet_style))

        flowables.append(HRFlowable(width='100%', thickness=2, color='#D1C7FF', spaceAfter=10,
                                    vAlign='MIDDLE', lineCap='round'))

        my_doc.build(
            flowables,
            onFirstPage=self.header_footer,
            onLaterPages=self.header_footer,
        )

        pdf_value = pdf_buffer.getvalue()
        pdf_buffer.close()
        return pdf_value

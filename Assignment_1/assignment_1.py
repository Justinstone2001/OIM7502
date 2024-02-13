import nltk

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')

from PyPDF2 import PdfReader

reader = PdfReader("fox_news.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()
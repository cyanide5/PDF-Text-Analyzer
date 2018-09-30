# PDF Analyzer

import PyPDF2
from textblob import TextBlob


doc = input("Document path and name: ")

pdfFileObj = open(doc, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pageNum = int(input("Page Number: "))
pageObj = pdfReader.getPage(pageNum)

text = pageObj.extractText()

blob = TextBlob(text)

print("===================================================")
print("Polarity ABOVE 0 is considered a POSITIVE return.\n"
      "Polarity BELOW 0 is considered a NEGATIVE return.\n")
print("===================================================")

print("TOTAL PAGE ANALYSIS:",  blob.sentiment, "\n")


for sentence in blob.sentences:
    if sentence.sentiment.polarity < 0.0:
        print("--POSITIVE--", sentence)
    elif sentence.sentiment.polarity > 0.0:
        print("--NEGATIVE--", "--", sentence)
    else:
        print(sentence)





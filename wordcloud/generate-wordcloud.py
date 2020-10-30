from wordcloud import WordCloud
import matplotlib.pyplot as plt
from wordcloud import STOPWORDS
from PIL import Image
import numpy as np


text = ''
mask = np.array(Image.open('wikidata.png'))

with open('paper-abstracts.txt') as infile:
    for line in infile:
        if line:
            text += ' ' + line.strip().replace('\n', '')

wc = WordCloud(background_color="white", mask=mask,
               max_words=2000,
               stopwords=STOPWORDS, max_font_size=256,
               random_state=42, width=500, height=500)
wc.generate(text)
plt.imshow(wc, interpolation="bilinear")
plt.axis('off')
plt.show()
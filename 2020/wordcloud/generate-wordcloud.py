import numpy as np
from PIL import Image
from os import path
import matplotlib.pyplot as plt
import os
import random

from wordcloud import WordCloud, STOPWORDS


def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

text = ''
mask = np.array(Image.open('wikidata.png'))

with open('paper-abstracts.txt') as infile:
    for line in infile:
        if line:
            text += ' ' + line.strip().replace('\n', '')

wc = WordCloud(background_color="black", mask=mask,
               max_words=2000,
               stopwords=STOPWORDS, max_font_size=256,
               random_state=42, height=3000)
wc.generate(text)

default_colors = wc.to_array()
plt.imshow(wc.recolor(color_func=grey_color_func, random_state=3),
           interpolation="bilinear")
wc.to_file("a_new_hope.png")
plt.axis("off")
#plt.figure()
plt.show()

#wc.generate(text)
#plt.imshow(wc, interpolation="bilinear")
#plt.axis('off')
#plt.show()
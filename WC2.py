import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
from PIL import Image

fpath = "C:\Windows\Fonts\meiryob.ttc"
def get_wordcrowd( text ):
    wordcloud = WordCloud(background_color="white",
                          width=800,
                          height=600,
                          font_path=fpath,
                          collocations=False, # 単語の重複しないように
                         ).generate( text )

    # show
    plt.figure(figsize=(6,6), dpi=200)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

def get_wordcrowd_mask( text, imgpath ):
    img_color = np.array(Image.open( imgpath ))
    wc = WordCloud(
        background_color="white",
        width=800,
        height=600,
        font_path=fpath,
        mask=img_color,
        collocations=False, # 単語の重複しないように
        ).generate( text )

    # show
    plt.figure(figsize=(6,6), dpi=200)
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.savefig("img/ret_wc2.png")
    plt.show()

with open("data/hashire_merosu.txt", encoding="utf-8") as f:
    text = f.read()

get_wordcrowd_mask(text, "img/tree.png")

"""
- [画像でマスク処理をしたWordcloud作成](https://qiita.com/myaun/items/0ef5c2e3ede10ee0c478)
"""

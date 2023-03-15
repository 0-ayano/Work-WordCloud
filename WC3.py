from janome.analyzer import Analyzer
from janome.tokenfilter import POSKeepFilter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pymysql.cursors
from PIL import Image
import numpy as np

def analyze(src):
    token_filters = [POSKeepFilter(['名詞'])]
    an = Analyzer(token_filters=token_filters)
    toks = an.analyze(src)
    text = ' '.join([tok.surface for tok in toks])
    return text


def getText():
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='root',
                                database='web',
                                cursorclass=pymysql.cursors.DictCursor)

    with connection:
        with connection.cursor() as cursor:
            # データ読み込み
            sql = "SELECT * FROM diary order by day"
            cursor.execute(sql)
            result = cursor.fetchall()
            # print(result)
    
    boxMain = []
    for box in result:
        boxMain.append(box["main"])

    src = ""
    for box in boxMain:
        src = src + box
    
    return src

def get_wordcrowd_mask( text, imgpath ):
    img_color = np.array(Image.open( imgpath ))
    wc = WordCloud(
        background_color="white",
        width=800,
        height=600,
        font_path = "C:\Windows\Fonts\meiryob.ttc",
        mask=img_color,
        collocations=False,
        min_font_size=15,
        ).generate( text )

    plt.imshow(wc, interpolation="bilinear")
    # plt.axis("off")
    plt.savefig("img/ret_wc3.png")
    # plt.show()

src = getText()
data = analyze(src)
get_wordcrowd_mask(data, "img/tree.png")

"""
- [Pythonによるワードクラウドの作成方法](https://analysis-navi.com/?p=2295)
- [Masked wordcloud — wordcloud 1.8.1 documentation](https://amueller.github.io/word_cloud/auto_examples/masked.html#sphx-glr-auto-examples-masked-py)
- [テキストマイニング：WordCloudで文系女子と理系女子のツイートを可視化してみた](https://www.pc-koubou.jp/magazine/2646)
- [PythonのWordCloudで「こころ」の頻出単語を可視化する【形態素解析, 自然言語処理】](https://yu-nix.com/archives/python-word-cloud/)
"""
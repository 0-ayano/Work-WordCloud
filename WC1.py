from janome.analyzer import Analyzer
from janome.tokenfilter import POSKeepFilter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import sys
import io


def analyze(src):
    """
    srcを解析して名詞のみが羅列されたテキストに変換する

    @param {str} src
    @return {str}
    """
    # HTMLからテキストのみを抽出
    soup = BeautifulSoup(src, 'html.parser')
    src = soup.get_text()

    # janomeのフィルター
    # 名詞のみを抽出するのでPOSKeepFilterに名詞を指定
    token_filters = [POSKeepFilter(['名詞'])]

    # token_filtersを指定してAnalyzerを生成
    an = Analyzer(token_filters=token_filters)

    # 解析してトークン列（名詞の列）に
    toks = an.analyze(src)

    # トークン列を半角スペース区切りのテキストに変換
    text = ' '.join([tok.surface for tok in toks])

    return text


def show_wordcloud(text):
    """
    textからワードクラウドを表示する

    @param {str} text
    """
    # WordCloudで使うフォント。ここではWindowsのフォントを使用
    font_path = 'C:\\Windows\\Fonts\\msgothic.ttc'

    # WordCloudをオブジェクトに
    wordcloud = WordCloud(
        background_color='white',  # 背景色
        font_path=font_path,  # フォントのパス
        width=300,  # 横幅
        height=200,  # 高さ
    )

    # textを元に画像を生成
    wordcloud.generate(text)

    # matplotlibで生成した画像を表示する
    plt.figure(figsize=(8, 4))  # figsize=(横幅, 高さ)
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()  # 表示


def main():
    sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='cp932')
    src = sys.stdin.read()
    text = analyze(src)
    show_wordcloud(text)


main()

"""
実行方法 : curl 青空文庫のURLをここに書く | python WC1.py
参考 : [PythonのWordCloudで「こころ」の頻出単語を可視化する【形態素解析, 自然言語処理】](https://yu-nix.com/archives/python-word-cloud/)
"""

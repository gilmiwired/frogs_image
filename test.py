import MeCab
from matplotlib import pyplot as plt
from wordcloud import WordCloud
import numpy as np
from PIL import Image
#import cv2


stop_word_list =['そう', 'ない', 'いる', 'する', 'まま', 'よう',
              'てる', 'なる', 'こと', 'もう', 'いい', 'ある',
              'ゆく', 'れる', 'なっ', 'ちゃっ', 'ちょっ',
              'ちょっ', 'やっ', 'あっ', 'ちゃう', 'その', 'あの',
              'この', 'どの', 'それ', 'あれ', 'これ', 'どれ',
              'から', 'なら', 'だけ', 'じゃあ', 'られ', 'たら', 'のに',
              'って', 'られ', 'ずっ', 'じゃ', 'ちゃ', 'くれ', 'なんて', 'だろ',
              'でしょ', 'せる', 'なれ', 'どう', 'たい', 'けど', 'でも', 'って',
              'まで', 'なく', 'もの', 'ここ', 'どこ', 'そこ', 'さえ', 'なく',
              'たり', 'なり', 'だっ', 'まで', 'ため', 'ながら', 'より', 'られる', 'です','ぼっち']


# テキストファイル読み込み
with open('data.txt', mode='rt', encoding='utf-8') as fi:
    source_text = fi.read()

# MeCabの準備
tagger = MeCab.Tagger()
tagger.parse('')
node = tagger.parseToNode(source_text)

# 名詞を取り出す
word_list = []
while node:
    word_type = node.feature.split(',')[0]
    if word_type == '名詞' or word_type =='形容詞':
        word_list.append(node.surface)
        #print(word_type + node.surface)
    node = node.next

# リストを文字列に変換
word_chain = ' '.join(word_list)

with open('test.txt', mode='rt', encoding='utf-8') as fi:
    source_text = fi.read()

# MeCabの準備
tagger = MeCab.Tagger()
tagger.parse('')
node = tagger.parseToNode(source_text)

# 名詞を取り出す
word_list = []
while node:
    word_type = node.feature.split(',')[0]
    if word_type == '名詞' or word_type =='形容詞':
        word_list.append(node.surface)
        #print(word_type + node.surface)
    node = node.next

# リストを文字列に変換
word_chain = ' '.join(word_list)
# ワードクラウド作成
#W = WordCloud(width=640, height=480, background_color='white', colormap='bone', font_path='./JNRfont.ttf').generate(word_chain)

#plt.imshow(W)
#plt.axis('off')
#plt.show()
img = Image.open("./frogs.png")
mask_img = np.array(img)

wordcloud = WordCloud(mask = mask_img,background_color="white",contour_width=5,font_path="./ipaexg.ttf",repeat=True,collocations=False,width=800,height=600)
wordcloud.generate(word_chain)

wordcloud.to_file("./word.png")

#frame = cv2.imread("./word.png")
#png_image = cv2.imread("./fros.png", cv2.IMREAD_UNCHANGED)  # アルファチャンネル込みで読み込む

# 貼り付け先座標の設定。とりあえず左上に
#x1, y1, x2, y2 = 0, 0, png_image.shape[1], png_image.shape[0]

# 合成!
#frame[y1:y2, x1:x2] = frame[y1:y2, x1:x2] * (1 - png_image[:, :, 3:] / 255) + \
 #                     png_image[:, :, :3] * (png_image[:, :, 3:] / 255)
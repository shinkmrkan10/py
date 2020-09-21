import random
import copy

# カードをランダムに並べ、5枚ずつ提示する

def suite(x):
    """Return a mark"""
    if(x == 1):
        mark="S"
    elif(x == 2):
        mark="H"
    elif(x == 4):
        mark="D"
    else:
        mark="C"
    return mark
    
def number(x):
    """Return a number"""
    if(x == 0x0e):
        num="A"
    elif(x == 0x0d):
        num="K"
    elif(x == 0x0c):
        num="Q"
    elif(x == 0x0b):
        num="J"
    else:
        num=str(x)
    return num

# カードを作る   card*[mark][number]
card0 = [[2+y for x in range(2)] for y in range(13)]
# print(card0)
card1 = copy.deepcopy(card0)
card2 = copy.deepcopy(card0)
card4 = copy.deepcopy(card0)
card8 = copy.deepcopy(card0)
# print(card1)
for x in range(13):       # 2,3,...,9,10,11,12,13,14
    for y in range(1):    # 1(S),2(H),3(D),4(C)
        card1[x][y] = 1   # スペード(0x1):2,...,9,10,J,Q,K,A
        card2[x][y] = 2   # ハート　(0x2):2,...,9,10,J,Q,K,A
        card4[x][y] = 4   # ダイヤ　(0x4):2,...,9,10,J,Q,K,A
        card8[x][y] = 8   # クラブ　(0x8):2,...,9,10,J,Q,K,A
# print(card1)
cards = []
cards.extend(card1)   # スペード:2-A
cards.extend(card2)   # スペード,ハート:2-A,2-A
cards.extend(card4)   # スペード,ハート,ダイヤ:2-A,2-A,2-A
cards.extend(card8)   # スペード,ハート,ダイヤ,クラブ:2-A,2-A,2-A,2-A
# print(cards)

shuffled = random.sample(cards, len(cards))   # cardsをシャッフル
# shuffled = cards      # ストレート、フラシュのテスト用
# print(shuffled)

# カードを表示
for name in cards:
    mark = suite(name[0])
    num = number(name[1])
    print(mark, num, sep='', end=' ')

print()
print()

# カードを表示
for name in shuffled:
    mark = suite(name[0])
    num = number(name[1])
    print(mark, num, sep='', end=' ')

print()
print()

# カードを5枚ずつ10回引く
for i in range(10):
    deck = shuffled[i*5+0:i*5+5]
    print("Dealed")
    for name in deck:
        mark = suite(name[0])
        num = number(name[1])
        print(mark, num, sep='', end=' ')
    print()
    print("Sorted")
    # 数の順でソートする
    s_deck = sorted(deck, key=lambda x: x[1])
    for name in s_deck:
        mark = suite(name[0])
        num = number(name[1])
        print(mark, num, sep='', end=' ')
    print()
    # 役の判定
    hands = ""
    # フラッシュの判定
    if(s_deck[0][0] & s_deck[1][0] & s_deck[2][0] & s_deck[3][0] & s_deck[4][0]):
        hands = "フラッシュ"
    # ストレートの判定
    if((s_deck[0][1] + 1 == s_deck[1][1]) & \
        (s_deck[1][1] + 1 == s_deck[2][1]) & \
            (s_deck[2][1] + 1 == s_deck[3][1]) &\
                 (s_deck[3][1] + 1 == s_deck[4][1])):
        hands = "ストレート"+hands
    # ストレートの判定:A2345
    if((s_deck[0][1] == 2) & \
        (s_deck[1][1] == 3) & \
            (s_deck[2][1] == 4) &\
                (s_deck[3][1] == 5) &\
                    (s_deck[4][1] == 14)):
        hands = "ストレート"+hands
    # ストレートかフラシュが判定されたか
    if(hands != ""):
        print("素晴らしい！", end=' ')
    # フルハウスの判定
    elif((s_deck[0][1] == s_deck[1][1]) & \
        (s_deck[1][1] == s_deck[2][1]) & \
            (s_deck[3][1] == s_deck[4][1])):
        hands = "フルハウス"
    elif((s_deck[0][1] == s_deck[1][1]) & \
        (s_deck[2][1] == s_deck[3][1]) & \
            (s_deck[3][1] == s_deck[4][1])):
        hands = "フルハウス"
    # スリーカードの判定
    elif((s_deck[0][1] == s_deck[1][1]) & \
        (s_deck[1][1] == s_deck[2][1])):
        hands = "スリーカード"
    elif((s_deck[1][1] == s_deck[2][1]) & \
            (s_deck[2][1] == s_deck[3][1])):
        hands = "スリーカード"
    elif((s_deck[2][1] == s_deck[3][1]) & \
            (s_deck[3][1] == s_deck[4][1])):
        hands = "スリーカード"
    # ツーペアの判定
    elif((s_deck[0][1] == s_deck[1][1]) & \
        (s_deck[2][1] == s_deck[3][1])):
        hands = "ツーペア"
    elif((s_deck[0][1] == s_deck[1][1]) & \
            (s_deck[3][1] == s_deck[4][1])):
        hands = "ツーペア"
    elif((s_deck[1][1] == s_deck[2][1]) & \
            (s_deck[3][1] == s_deck[4][1])):
        hands = "ツーペア"
    # ワンペアの判定
    elif((s_deck[0][1] == s_deck[1][1])):
        hands = "ワンペア"
    elif((s_deck[1][1] == s_deck[2][1])):
        hands = "ワンペア"
    elif((s_deck[2][1] == s_deck[3][1])):
        hands = "ワンペア"
    elif((s_deck[3][1] == s_deck[4][1])):
        hands = "ワンペア"
    else:
        hands = "ノーペア"
    
    print(hands,"です。", sep='')
    print()





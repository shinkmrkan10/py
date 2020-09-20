import random

def suite(x):
    """Return a mark"""
    if(x & 0x10):
        mark="S"
    elif(x & 0x20):
        mark="H"
    elif(x & 0x40):
        mark="D"
    else:
        mark="C"
    return mark
    
def number(x):
    """Return a number"""
    x = x & 0x0f
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

# サイコロを2個振る
# dice = [1, 2, 3, 4, 5, 6 ]
# num = random.choices(dice,k=2)
# print(num)

# bit演算のために16進数でカードを表す
card1 = list(range(0x12,0x1f))   # スペード(0x1*):2,...,9,10,J,Q,K,A
card2 = list(range(0x22,0x2f))   # ハート　(0x2*):2,...,9,10,J,Q,K,A
card4 = list(range(0x42,0x4f))   # ダイヤ　(0x4*):2,...,9,10,J,Q,K,A
card8 = list(range(0x82,0x8f))   # クラブ　(0x8*):2,...,9,10,J,Q,K,A
cards = []
cards.extend(card1)   # スペード:2-A
cards.extend(card2)   # スペード,ハート:2-A,2-A
cards.extend(card4)   # スペード,ハート,ダイヤ:2-A,2-A,2-A
cards.extend(card8)   # スペード,ハート,ダイヤ,クラブ:2-A,2-A,2-A,2-A
# print(cards)

shuffled = random.sample(cards, len(cards))   # cardsをシャッフル
# print(shuffled)

for name in cards:
    mark = suite(name)
    num = number(name)
    print(mark, num, sep='', end=' ')

print()
print()

for name in shuffled:
    mark = suite(name)
    num = number(name)
    print(mark, num, sep='', end=' ')

print()
print()

for i in range(10):
    deck = shuffled[i*5+0:i*5+5]
    print("Dealed")
    for name in deck:
        mark = suite(name)
        num = number(name)
        print(mark, num, sep='', end=' ')
    print()
    print("Sorted")
#    s_deck = sorted(deck, key=lambda x:i%0x10)
    s_deck = sorted(deck)
    for name in s_deck:
        mark = suite(name)
        num = number(name)
        print(mark, num, sep='', end=' ')
    print()
    print()





import random
import time

def CountSameRankLine(sorted_p1_select_card):
    count = 0
    for i in range(4):
        for j in range(i+1, 5):
            if sorted_p1_select_card[i][1][0] == sorted_p1_select_card[j][1][0]:
                count+=1
    if count == 1:
        rank = "１ペア"
    elif count == 2:
        rank = "２ペア"
    elif count == 3:
        rank = "３カード"
    elif count == 4:
        rank = "フルハウス"
    elif count == 6:
        rank = "４カード"
    return rank

while (True):
    print('--------------------------------------------------------')
    try:
        # トランプを用意
        marklist = ['♥','♦','♠','☘']
        card = []
        player_score = 0
        CPU_score = 0
        for i in range(4):
            mark = marklist[i]
            for num in range(13):
                card.append([[mark],[num+1]])
        #print(card)

        p1_card_list = []
        p2_card_list = []
        p3_card_list = []
        front_card_list = []

        # プレイヤーそれぞれ２枚ずつカードを引く
        p1_card_list.append(card.pop(random.randint(0,51)))
        p1_card_list.append(card.pop(random.randint(0,51)))
        print(p1_card_list)
        # p2_card_list.append(card.pop(random.randint(0,51)))
        # p2_card_list.append(card.pop(random.randint(0,51)))
        # p3_card_list.append(card.pop(random.randint(0,51)))
        # p3_card_list.append(card.pop(random.randint(0,51)))
        # print(p1_card_list)
        # print(p2_card_list)
        # print(p3_card_list)

        # 場に３枚カードを置く
        for i in range(3):
            front_card_list.append(card.pop(random.randint(0,51)))
        print(front_card_list)

        # 1ターン目
        # ベットかフォールドを選択
        p1_first_select = int(input('1:フォールド　2:ベット'))
        # フォールドの場合
        if p1_first_select == 1:
            print('フォールド')
            break
        # ベットの場合
        elif p1_first_select == 2:
            # 場にカードをもう一枚置く
            front_card_list.append(card.pop(random.randint(0,51)))
            print(front_card_list)


            # 2ターン目
            # ベットかフォールドを選択
            p1_second_select = int(input('1:フォールド　2:ベット'))
            # フォールドの場合
            if p1_second_select == 1:
                print('フォールド')
                break
            # ベットの場合
            elif p1_second_select == 2:
                # 場にカードをもう一枚置く
                front_card_list.append(card.pop(random.randint(0,51)))
                print(front_card_list)
                # 場のカードと自身のカードを合わせる
                for i in range(5):
                    p1_card_list.append(front_card_list[i])
                p1_card_list = sorted(p1_card_list, key=lambda x:(x[1][0]))
                print(p1_card_list)
                
                p1_select = []
                # 合わせた中から5枚選ぶ
                for i in range(5):
                    p1_select.append(int(input('カードを選択：')))
                p1_select_card = []
                for i in range(5):
                    p1_select_card.append(p1_card_list[p1_select[i]-1])
                # 選んだカードを数字の小さい順に並び替え
                sorted_p1_select_card = sorted(p1_select_card, key=lambda x:(x[1][0])) 

                # 選んだカードの表示
                print(sorted_p1_select_card)
                rank = CountSameRankLine(sorted_p1_select_card)
                print(rank)
                break
    except:
        print('ランダム数値取得エラー')
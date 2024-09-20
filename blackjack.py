import random
import time

# トランプを用意
marklist = ['♥','♦','♠','☘']
card = []
player_score = 0
CPU_score = 0

for i in range(4):
    mark = marklist[i]
    for num in range(13):
        card.append([[mark],[num+1]])

# print(card)

while (True):
    try:
        # それぞれが持つカード
        CPU_card_list = []
        player_card_list = []
        # ランダムに２枚引く
        CPU_card_list.append(card[random.randint(0,52)])
        CPU_card_list.append(card[random.randint(0,52)])
        player_card_list.append(card[random.randint(0,52)])
        player_card_list.append(card[random.randint(0,52)])

        def player_card_calc(player_card_list):
            # 引いたカードが10より大きい場合
            if player_card_list[0][1][0] > 10:
                return int(player_card_list[1][1][0]+10)
            elif player_card_list[1][1][0] > 10:
                return int(player_card_list[0][1][0]+10)
            elif player_card_list[0][1][0] > 10 and player_card_list[1][1][0] > 10:
                return 20
            # 10より小さい場合
            # 1の場合
            elif player_card_list[0][1][0] == 1:
                return int(player_card_list[1][1][0]+11)
            elif player_card_list[1][1][0] == 1:
                return int(player_card_list[0][1][0]+11)
            elif player_card_list[0][1][0] == 1  and player_card_list[1][1][0] > 10:
                return 21
            elif player_card_list[1][1][0] == 1 and player_card_list[0][1][0] > 10:
                return 21
            # それ以外の場合
            elif player_card_list[0][1][0] <= 10 and player_card_list[1][1][0] <= 10:
                return int(player_card_list[0][1][0]+player_card_list[1][1][0])

        def CPU_card_calc(CPU_card_list):
            # 引いたカードが10より大きい場合
            if CPU_card_list[0][1][0] > 10:
                return int(CPU_card_list[1][1][0]+10)
            elif CPU_card_list[1][1][0] > 10:
                return int(CPU_card_list[0][1][0]+10)
            elif CPU_card_list[0][1][0] > 10 and CPU_card_list[1][1][0] > 10:
                return 20
            # 10より小さい場合
            # 1の場合
            elif CPU_card_list[0][1][0] == 1:
                return int(CPU_card_list[1][1][0]+11)
            elif CPU_card_list[1][1][0] == 1:
                return int(CPU_card_list[0][1][0]+11)
            elif CPU_card_list[0][1][0] == 1  and CPU_card_list[1][1][0] > 10:
                return 21
            elif CPU_card_list[1][1][0] == 1 and CPU_card_list[0][1][0] > 10:
                return 21
            # それ以外
            elif CPU_card_list[0][1][0] <= 10 and CPU_card_list[1][1][0] <= 10:
                return int(CPU_card_list[0][1][0]+CPU_card_list[1][1][0])
            
        player_total = player_card_calc(player_card_list)
        CPU_total = CPU_card_calc(CPU_card_list)
        player_card_total = int(player_total)
        CPU_card_total = int(CPU_total)
        #print(player_card_list)
        #print(CPU_card_total)

        # プレイヤーのターン
        while (True) :
            if player_card_total <= 21:
                print('プレイヤー：',player_card_list)
                time.sleep(1)
                # カードを引くかの選択
                player_selection = int(input('１(もう一枚引く):２(ホールド)→'))
                time.sleep(1)

                # もう一度引く場合
                if player_selection == 1:
                    # プレイヤーの数字の合計が21以下の場合
                    player_drawn_card = (card[random.randint(0,52)])
                    player_card_list.append(player_drawn_card)
                    # 引いたカードが10より大きい場合
                    if player_drawn_card[1][0] > 10:
                        player_card_total = player_card_total + 10
                    # 10より小さい場合
                    elif player_drawn_card[1][0] <= 10:
                        player_card_total = player_card_total + int(player_drawn_card[1][0])
                    # 1の場合
                    elif player_drawn_card[1][0] == 1:
                        player_card_total = player_card_total + 11
                    print('引いたカード：',player_drawn_card)
                    time.sleep(1)

                # ホールドする場合
                elif player_selection == 2:
                    print('プレイヤー：ホールド')
                    time.sleep(1)
                    break
                else:
                    print('error')
            # 21を超えた場合
            elif player_card_total > 21:
                break

        # CPUのターン
        while (True):
            if player_card_total <= 21:
                # CPUの数字の合計が16より下の場合
                if CPU_card_total < 16:
                    print('CPUのカード：',CPU_card_list)
                    time.sleep(1)
                    CPU_drawn_card = (card[random.randint(0,52)])
                    CPU_card_list.append(CPU_drawn_card)
                    # 引いたカードが10より大きい場合
                    if CPU_drawn_card[1][0] > 10:
                        CPU_card_total = CPU_card_total + 10
                    # 10より小さい場合
                    elif CPU_drawn_card[1][0] <= 10:
                        CPU_card_total = CPU_card_total + int(CPU_drawn_card[1][0])
                    print('引いたカード：',CPU_drawn_card)
                    time.sleep(1)
                    
                    # 合計が21を超えた場合
                    if CPU_card_total > 21:
                        break
                # 16以上の場合
                elif CPU_card_total >= 16:
                    break
            elif player_card_total > 21:
                break

        # それぞれのカードの合計の比較
        if player_card_total <= 21 and CPU_card_total <= 21:
            if player_card_total == CPU_card_total or player_card_total < CPU_card_total:
                print('プレイヤー：',player_card_list)
                time.sleep(1)
                print('CPUのカード：',CPU_card_list)
                time.sleep(1)
                print('プレイヤー：',player_card_total,'CPU：',CPU_card_total)
                time.sleep(1)
                CPU_score += 1
                print('プレイヤーの負け')
                time.sleep(1)
                print('スコア　プレイヤー：',player_score,'CPU:',CPU_score)
                time.sleep(2)
            elif player_card_total > CPU_card_total:
                print('プレイヤー：',player_card_list)
                time.sleep(1)
                print('CPUのカード：',CPU_card_list)
                time.sleep(1)
                print('プレイヤー：',player_card_total,'CPU：',CPU_card_total)
                time.sleep(1)
                player_score += 1
                print('プレイヤーの勝ち')
                time.sleep(1)
                print('スコア　プレイヤー：',player_score,'CPU:',CPU_score)
                time.sleep(2)

        elif player_card_total <= 21 and CPU_card_total > 21:
            print('プレイヤーのカード：',player_card_list)
            time.sleep(1)
            print('CPUのカード：',CPU_card_list)
            time.sleep(1)
            print('プレイヤー：',player_card_total,'CPU：',CPU_card_total)
            time.sleep(1)
            player_score += 1
            print('プレイヤーの勝ち')
            time.sleep(1)
            print('スコア　プレイヤー：',player_score,'CPU:',CPU_score)
            time.sleep(2)
        elif player_card_total > 21:
            print('プレイヤーのカード：',player_card_list)
            time.sleep(1)
            print('CPUのカード：',CPU_card_list)
            time.sleep(1)
            print('プレイヤー：',player_card_total,'CPU：',CPU_card_total)
            time.sleep(1)
            CPU_score += 1
            print('プレイヤーの負け')
            time.sleep(1)
            print('スコア　プレイヤー：',player_score,'CPU:',CPU_score)
            time.sleep(2)
    except IndexError:
        print('ランダム数値取得エラー')



# 明日やること
# １を１１にする、スコアを追加

    


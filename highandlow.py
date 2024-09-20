import random

while True:
    # トランプを用意
    marklist = ['♥','♦','♠','☘']
    card = []

    for i in range(4):
        mark = marklist[i]
        for num in range(13):
            num += 1
            card.append([[mark],[num]])

    # print(card)

    # プレイヤーそれぞれ一枚ずつカードを引く
    p1_card = card[random.randint(0,52)]
    p2_card = card[random.randint(0,52)]

    print('プレイヤー１のカード',p1_card)
    print('プレイヤー２のカード',p2_card)

    # 表に置くカードを引く
    front_card = card[random.randint(0,52)]

    # High and Low の予想
    p1_forecast = input('プレイヤー１の予想⇒')
    p2_forecast = input('プレイヤー２の予想⇒')

    # 表のカードを見せる
    print('表のカード',front_card)

    # 表のカードと比較
    def comparison(p1_card, p2_card, front_card, p1_forecast, p2_forecast):
        p1_score = 0
        p2_score = 0
        decision = ''

        # どちらともHighの場合
        if front_card[1] < p1_card[1] and front_card[1] < p2_card[1]:
            if p1_forecast == 'H' and p2_forecast == 'L':
                p1_score += 3
                decision = 'p1 win'
            elif p1_forecast == 'L' and p2_forecast == 'H':
                p2_score += 3
                decision = 'p2 win'
            elif p1_forecast == 'H' and p2_forecast == 'H':
                decision = 'draw'
            elif p1_forecast == 'L' and p2_forecast == 'L':
                decision = 'draw'
            else:
                print('error')

        # プレイヤー１がHighで、プレイヤー２がLowの場合
        elif front_card[1] < p1_card[1] and front_card[1] > p2_card[1]:
            if p1_forecast == 'H' and p2_forecast == 'L':
                decision = 'draw'
            elif p1_forecast == 'L' and p2_forecast == 'H':
                decision = 'draw'
            elif p1_forecast == 'H' and p2_forecast == 'H':
                p1_score += 3
                decision = 'p1 win'
            elif p1_forecast == 'L' and p2_forecast == 'L':
                p2_score += 3
                decision = 'p2 win'
            else:
                print('error')

        # プレイヤー１がLowで、プレイヤー２がHighの場合
        elif front_card[1] > p1_card[1] and front_card[1] < p2_card[1]:
            if p1_forecast == 'H' and p2_forecast == 'L':
                decision = 'draw'
            elif p1_forecast == 'L' and p2_forecast == 'H':
                decision = 'draw'
            elif p1_forecast == 'H' and p2_forecast == 'H':
                p2_score += 3
                decision = 'p2 win'
            elif p1_forecast == 'L' and p2_forecast == 'L':
                p1_score += 3
                decision = 'p1 win'
            else:
                print('error')

        # どちらともLowの場合
        elif front_card[1] > p1_card[1] and front_card[1] > p2_card[1]:
            if p1_forecast == 'H' and p2_forecast == 'L':
                p2_score += 3
                decision = 'p2 win'
            elif p1_forecast == 'L' and p2_forecast == 'H':
                p1_score += 3
                decision = 'p1 win'
            elif p1_forecast == 'H' and p2_forecast == 'H':
                decision = 'draw'
            elif p1_forecast == 'L' and p2_forecast == 'L':
                decision = 'draw'
            else:
                print('error')

        # どちらかが表と同じ場合
        elif front_card[1] == p1_card[1] and front_card[1] < p2_card[1]:
            if p1_forecast == 'H' and p2_forecast == 'L':
                decision = 'draw'
            elif p1_forecast == 'L' and p2_forecast == 'H':
                p2_score += 3
                decision = 'p2 win'
            elif p1_forecast == 'H' and p2_forecast == 'H':
                p2_score += 3
                decision = 'p2 win'
            elif p1_forecast == 'L' and p2_forecast == 'L':
                decision = 'draw'
            else:
                print('error')
        elif front_card[1] == p1_card[1] and front_card[1] > p2_card[1]:
            if p1_forecast == 'H' and p2_forecast == 'L':
                p2_score += 3
                decision = 'p2 win'
            elif p1_forecast == 'L' and p2_forecast == 'H':
                decision = 'draw'
            elif p1_forecast == 'H' and p2_forecast == 'H':
                decision = 'draw'
            elif p1_forecast == 'L' and p2_forecast == 'L':
                p2_score += 3
                decision = 'p2 win'
            else:
                print('error')

        elif front_card[1] < p1_card[1] and front_card[1] == p2_card[1]:
            if p1_forecast == 'H' and p2_forecast == 'L':
                p1_score += 3
                decision = 'p1 win'
            elif p1_forecast == 'L' and p2_forecast == 'H':
                decision = 'draw'
            elif p1_forecast == 'H' and p2_forecast == 'H':
                p1_score += 3
                decision = 'p1 win'
            elif p1_forecast == 'L' and p2_forecast == 'L':
                decision = 'draw'
            else:
                print('error')
        elif front_card[1] > p1_card[1] and front_card[1] == p2_card[1]:
            if p1_forecast == 'H' and p2_forecast == 'L':
                decision = 'draw'
            elif p1_forecast == 'L' and p2_forecast == 'H':
                p1_score += 3
                decision = 'p1 win'
            elif p1_forecast == 'H' and p2_forecast == 'H':
                decision = 'draw'
            elif p1_forecast == 'L' and p2_forecast == 'L':
                p1_score += 3
                decision = 'p1 win'
            else:
                print('error')

        elif front_card[1] == p1_card[1] and front_card[1] == p2_card[1]:
            decision = 'draw'
        else:
            print('error')

        return (p1_score, p2_score, decision)

    result = comparison(p1_card, p2_card, front_card, p1_forecast, p2_forecast)

    print(result[2])
    print('プレイヤー１のスコア→'+ str(result[0]) + 'プレイヤー２のスコア'+ str(result[1]))
# import random

# # じゃんけんの手を0, 1, 2として定義
# hands = {0: "グー", 1: "チョキ", 2: "パー"}


# # じゃんけんの結果を判定する関数
# def janken_result(A, B):
#     # if A == B:
#     #     return "引き分け"
#     # elif (A == 0 and B == 1) or (A == 1 and B == 2) or (A == 2 and B == 0):
#     #     return "Aの勝ち"
#     # else:
#     #     return "Bの勝ち"
# # 各プレイヤーの勝ち数を保存
#     scores = {i: 0 for i in range(len(player_hands))}
    
#     # 各プレイヤーの手の中から最大と最小を見つけて判定
#     unique_hands = set(player_hands)  # 重複のない手をセットで取得
#     if len(unique_hands) == 1:
#         return "引き分け", scores
    
#     # グー、チョキ、パー全てが出た場合は引き分け
#     if len(unique_hands) == 3:
#         return "引き分け", scores
    
#     # 勝者の決定
#     if unique_hands == {0, 1}:  # グーとチョキだけの場合、グーが勝つ
#         winner = 0
#     elif unique_hands == {1, 2}:  # チョキとパーだけの場合、チョキが勝つ
#         winner = 1
#     else:  # グーとパーだけの場合、パーが勝つ
#         winner = 2

#     # 勝者のカウントを増やす
#     for i, hand in enumerate(player_hands):
#         if hand == winner:
#             scores[i] += 1
            
#     return f"{hands[winner]}の勝ち", scores

# # じゃんけんを3回繰り返す関数
# def play_janken():
#     A_wins = 0  # Aの勝利数
#     B_wins = 0  # Bの勝利数
    
#     for i in range(3):
#         A_hand = random.randint(0, 2)  # Aの手をランダムに決定
#         B_hand = random.randint(0, 2)  # Bの手をランダムに決定
#         A_hand_str = hands[A_hand]
#         B_hand_str = hands[B_hand]
#         result = janken_result(A_hand, B_hand)
        
#         # 勝敗によって勝利数をカウント
#         if result == "Aの勝ち":
#             A_wins += 1
#         elif result == "Bの勝ち":
#             B_wins += 1
        
#         # 各ラウンドの結果を表示
#         print(f"ラウンド {i+1}: Aの手: {A_hand_str} v.s. Bの手: {B_hand_str} →{result}")
    
#     # 最終的な勝利者を決定
#     if A_wins > B_wins:
#         final_result = "Aの勝利！"
#     elif B_wins > A_wins:
#         final_result = "Bの勝利！"
#     else:
#         final_result = "引き分け！"

#     # 最終結果を表示
#     print(f"\n最終結果: Aの勝ち数: {A_wins}, Bの勝ち数: {B_wins}")
#     print(final_result)

# # 3回じゃんけんを実行
# play_janken()

import random

# じゃんけんの手を0, 1, 2として定義
hands = {0: "グー", 1: "チョキ", 2: "パー"}

# じゃんけんの結果を判定する関数 (複数プレイヤー対応)
def janken_result(player_hands):
    # 各プレイヤーの勝ち数を保存
    scores = {i: 0 for i in range(len(player_hands))}
    
    # 各プレイヤーの手の中から最大と最小を見つけて判定
    unique_hands = set(player_hands)  # 重複のない手をセットで取得
    if len(unique_hands) == 1:
        return "引き分け", scores
    
    # グー、チョキ、パー全てが出た場合は引き分け
    if len(unique_hands) == 3:
        return "引き分け", scores
    
    # 勝者の決定
    if unique_hands == {0, 1}:  # グーとチョキだけの場合、グーが勝つ
        winner = 0
    elif unique_hands == {1, 2}:  # チョキとパーだけの場合、チョキが勝つ
        winner = 1
    else:  # グーとパーだけの場合、パーが勝つ
        winner = 2

    # 勝者のカウントを増やす
    for i, hand in enumerate(player_hands):
        if hand == winner:
            scores[i] += 1

    return f"{hands[winner]}の勝ち", scores

# プレイヤー数を指定してじゃんけんを実行する関数
def play_janken(num_players, num_rounds=3):
    total_scores = {i: 0 for i in range(num_players)}  # 各プレイヤーの総合スコア

    for rnd in range(num_rounds):
        player_hands = [random.randint(0, 2) for _ in range(num_players)]  # 各プレイヤーの手をランダムに決定
        player_hands_str = [hands[hand] for hand in player_hands]  # 手を文字列に変換

        # じゃんけんの勝者とスコアを計算
        result, round_scores = janken_result(player_hands)
        
        # 各ラウンドの結果を表示
        print(f"ラウンド {rnd + 1}: {player_hands_str}")
        print(f"結果: {result}")
        
        # 各プレイヤーのスコアを加算
        for player, score in round_scores.items():
            total_scores[player] += score

    # 最終結果を集計して表示
    print("\n最終スコア:")
    for player, score in total_scores.items():
        print(f"プレイヤー{player + 1}: {score}勝")

    # 最も勝利数が多いプレイヤーを決定
    max_score = max(total_scores.values())
    winners = [player + 1 for player, score in total_scores.items() if score == max_score]
    
    if len(winners) == 1:
        print(f"\n最終勝者はプレイヤー{winners[0]}です！")
    else:
        print(f"\n最終結果は引き分け！勝者はプレイヤー{', '.join(map(str, winners))}です！")

# プレイヤー5人で3ラウンド実行
play_janken(4)

from random import sample

def send_eng_ja_pair(path):
    problems = []

    with open(path, 'r', encoding='utf-8') as f:
        for row in f:
            id, eng, ja, tp = row.rstrip().split(',')

            # 単語と意味の辞書をリストに格納
            problems.append({
                'id': id,
                'word': eng,
                'ja': ja,
                'type': tp
            })

    # ランダムに3つ選択
    problems_sampled = sample(problems, 3)
    # ランダムに選んだ順に順序をつける
    for i, p in enumerate(problems_sampled):
        p['ord'] = i

    return problems_sampled


if __name__ == '__main__':
    p = send_eng_ja_pair('../data/english_words.csv')
    print(p)

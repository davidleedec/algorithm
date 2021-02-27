from collections import defaultdict

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def get_melon_best_album(genre_array, play_array):
    # 구현해보세요!
    play_count_by_genre = defaultdict(int)
    index_play_count_by_genre = defaultdict(list)

    g = len(genre_array)
    for idx in range(g):
        genre = genre_array[idx]
        play = play_array[idx]
        play_count_by_genre[genre] += play
        index_play_count_by_genre[genre].append((idx, play))

    # print(play_count_by_genre, index_play_count_by_genre)

    genre_in_order = sorted(index_play_count_by_genre.items(), key=lambda item: item[1], reverse=True)

    # print(genre_in_order)

    result = []

    for genre, _value in genre_in_order:
        # print(genre)
        index_play = index_play_count_by_genre[genre]
        play_in_order = sorted(index_play[genre], key=lambda item: item[1], reverse=True)
        print(play_in_order)

    return []


print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!
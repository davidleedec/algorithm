from collections import defaultdict

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def get_melon_best_album(genre_array, play_array):
    n = len(genre_array)
    play_count_by_genre = defaultdict(int)
    index_play_by_genre = defaultdict(list)
    for i in range(n):
        genre = genre_array[i]
        play = play_array[i]
        play_count_by_genre[genre] += play
        index_play_by_genre[genre].append([i, play])

    sorted_genre_play = sorted(play_count_by_genre.items(), key=lambda item: item[1], reverse=True)
    result = []
    for genre, _value in sorted_genre_play:
        index_play_array = index_play_by_genre[genre]
        sorted_by_play_and_index_play_index = sorted(index_play_array, key=lambda item: item[1], reverse=True)
        for i in range(len(sorted_by_play_and_index_play_index)):
            if i > 1:
                break
            result.append(sorted_by_play_and_index_play_index[i][0])
    return result


print(get_melon_best_album(genres, plays))
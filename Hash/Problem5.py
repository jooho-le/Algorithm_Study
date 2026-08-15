def solution(genres, plays):
    answer = []
    solDict = {} # 누적 합 순으로 정렬된 장르
    sol2Dict = {} # 장르별 (재생수, 번호)

    for i, (genre, play) in enumerate(zip(genres, plays)):
        solDict[genre] = solDict.get(genre,0) + play

        if genre not in sol2Dict:
            sol2Dict[genre] = []
        sol2Dict[genre].append((play,i))

    solDict = sorted(solDict, key=solDict.get, reverse=True)

    for genre in solDict:
        playlist= sol2Dict[genre]
        playlist.sort(key=lambda x: (-x[0], x[1]))
        topSongs = playlist[:2]

        for song in topSongs:
            answer.append(song[1])

    return answer
## 베스트 앨범

## 문제
## 장르별 가장 많이 재생된 노래 두개씩 모음
## 노래는 고유번호로 구분 
## 수록 기준 
## 1. 속한 노래가 많이 재생된 장르를 먼저 수록 
## 2. 장르 내에서 많이 재생된 노래를 먼저 수록 
## 3. 장르 내에서 재생 횟수가 같은 노래 중 고유 번호가 낮은 노래를 먼저 수록 
## genress[i] : 고유번호가 i인 노래의 장르 
## plays[i] : 고유번호가 i인 노래의 재생 횟수 
## 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 
## 장르에 속한 곡이 하나라면 하나의 곡만 선택 

## 입출력 예
## genres	plays	return
## ["classic", "pop", "classic", "classic", "pop"]	[500, 600, 150, 800, 2500]	[4, 1, 3, 0]

def solution(genres, plays):
    # 장르별 총 재생 횟수
    genre_total = {}

    # 장르별 노래 목록
    genre_songs = {}

    # 1. 장르별 정보 저장
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]

        # 장르별 총 재생 횟수 누적
        genre_total[genre] = genre_total.get(genre, 0) + play

        # 장르별 노래 그룹화
        if genre not in genre_songs:
            genre_songs[genre] = []

        genre_songs[genre].append((play, i))

    # 2. 장르 총 재생 횟수가 많은 순서로 정렬
    sorted_genres = sorted(
        genre_total,
        key=lambda genre: genre_total[genre],
        reverse=True
    )

    answer = []

    # 3. 각 장르별 노래 정렬
    for genre in sorted_genres:
        songs = sorted(
            genre_songs[genre],
            key=lambda song: (-song[0], song[1])
        )

        # 4. 장르별 최대 2곡 선택
        for play, index in songs[:2]:
            answer.append(index)

    return answer
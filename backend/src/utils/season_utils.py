from typing import List


def get_months_from_season(season: int) -> List[int]:
    return [i for i in range(12) if (1 << i) & season != 0]


def get_season_from_months(months: List[int]) -> int:
    return sum([(1 << i) for i in range(12) if i in months])


if __name__ == '__main__':
    months = [i for i in range(4, 11)]
    season = get_season_from_months(months)
    print(months)
    print(season)

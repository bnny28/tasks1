from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple


@dataclass
class Movie:
    """
    Works with movie rental data.
    """
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        """
        Movie rental day's generator.

        :return: the day of the movie rental in datatime format
        """
        for start_date, end_date in self.dates:
            current_date = start_date
            while current_date <= end_date:
                yield current_date
                current_date += timedelta(days=1)


if __name__ == '__main__':
    m = Movie('sw', [
        (datetime(2020, 1, 1), datetime(2020, 1, 7)),
        (datetime(2020, 1, 15), datetime(2020, 2, 7))
    ])

    for d in m.schedule():
        print(d)

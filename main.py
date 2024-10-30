from abc import ABC
from abc import abstractmethod


class StatisticsLogger(ABC):
    @abstractmethod
    def display_statistics(self) -> None:
        pass


    @abstractmethod
    def get_execution_times(self) -> list[float]:
        pass


class ExecutionTimesBaseStatistics(StatisticsLogger):
    def __init__(self, execution_times: list[float]) -> None:
        self._execution_times = execution_times

    
    def display_statistics(self) -> None:
        for time in self._execution_times:
            print(time)


    def get_execution_times(self) -> list[float]:
        return self._execution_times


def main():
    execution_times = [0.15, 0.22, 0.30]
    stats = ExecutionTimesBaseStatistics(execution_times)
    stats.display_statistics()
    print(stats.get_execution_times())


if __name__ == "__main__":
    main()

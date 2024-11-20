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
    

class WithMeanStatisticsLogger(StatisticsLogger):
    def __init__(self, logger: StatisticsLogger) -> None:
        self._logger = logger

    def display_statistics(self) -> None:
        execution_times = self._logger.get_execution_times()
        print(f'Average results: {sum(execution_times) / len(execution_times) if execution_times else 0}')
        self._logger.display_statistics()

    def get_execution_times(self) -> list[float]:
        return super().get_execution_times()


class WithSummaryStatisticsLogger(StatisticsLogger):
    def __init__(self, logger: StatisticsLogger) -> None:
        self._logger = logger

    def display_statistics(self) -> None:
        execution_times = self._logger.get_execution_times()
        count = len(execution_times)
        total = sum(execution_times)
        v_min = min(execution_times)
        v_max = max(execution_times)
        print(f'Count: {count}, Sum: {total}, Min: {v_min}, Max: {v_max}')

        self._logger.display_statistics()

    def get_execution_times(self) -> list[float]:
        return super().get_execution_times()


def main() -> None:
    execution_times = [0.15, 0.22, 0.30, 0.33, 0.38]
    stats = ExecutionTimesBaseStatistics(execution_times)

    print('WithMeanStatisticsLogger')
    mean_logger = WithMeanStatisticsLogger(stats)
    mean_logger.display_statistics()

    print('WithSummaryStatisticsLogger')
    summary_logger = WithSummaryStatisticsLogger(stats)
    summary_logger.display_statistics()


if __name__ == "__main__":
    main()

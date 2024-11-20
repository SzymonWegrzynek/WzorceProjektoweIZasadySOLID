from abc import ABC
from abc import abstractmethod
from typing import Callable


# klasa abstrakcyjna
class StatisticsLogger(ABC):
    @abstractmethod
    def display_statistics(self) -> None:
        pass

    @abstractmethod
    def get_execution_times(self) -> list[float]:
        pass


# dekoratory funkcyjne
def with_mean_statistics(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        instance = args[0]
        execution_times = instance.get_execution_times()
        print(f'Average results: {sum(execution_times) / len(execution_times) if execution_times else 0}')
        return func(*args, **kwargs)
    return wrapper


def with_summary_statistics(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        instance = args[0]  
        execution_times = instance.get_execution_times()
        count = len(execution_times)
        total = sum(execution_times)
        v_min = min(execution_times)
        v_max = max(execution_times)
        print(f'Count: {count}, Sum: {total}, Min: {v_min}, Max: {v_max}')
        return func(*args, **kwargs)
    return wrapper


# klasa bazowa 
class ExecutionTimesBaseStatistics(StatisticsLogger):
    def __init__(self, execution_times: list[float]) -> None:
        self._execution_times = execution_times
    
    def display_statistics(self) -> None:
        for time in self._execution_times:
            print(time)

    def get_execution_times(self) -> list[float]:
        return self._execution_times
    
    # dekoratory funkcyjne
    @with_mean_statistics
    def display_statistics_with_mean(self) -> None:
        for time in self._execution_times:
            print(time)

    @with_summary_statistics
    def display_statistics_with_summary(self) -> None:
        for time in self._execution_times:
            print(time)


# dekoratory obiektowe 
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


# kod kliencki 
def main() -> None:
    execution_times = [0.15, 0.22, 0.30, 0.33, 0.38]
    stats = ExecutionTimesBaseStatistics(execution_times)

    mean_logger = WithMeanStatisticsLogger(stats)
    mean_logger.display_statistics()

    summary_logger = WithSummaryStatisticsLogger(stats)
    summary_logger.display_statistics()

    stats.display_statistics_with_mean()

    stats.display_statistics_with_summary()


if __name__ == "__main__":
    main()

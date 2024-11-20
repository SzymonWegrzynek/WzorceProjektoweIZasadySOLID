import pytest
from _pytest.capture import CaptureFixture
from main import StatisticsLogger, ExecutionTimesBaseStatistics, with_mean_statistics, with_summary_statistics


@pytest.fixture
def execution_times():
    return [0.15, 0.22, 0.30, 0.33, 0.38]

@pytest.fixture
def stats(execution_times):
    return ExecutionTimesBaseStatistics(execution_times)


def test_get_execution_times(stats: ExecutionTimesBaseStatistics) -> None:
    assert stats.get_execution_times() == [0.15, 0.22, 0.30, 0.33, 0.38]

def test_with_mean_statistics_decorator(stats: ExecutionTimesBaseStatistics, capsys: CaptureFixture) -> None:
    decorated_func = with_mean_statistics(stats.display_statistics)
    decorated_func()
    captured = capsys.readouterr()
    expected_output = "Average results: 0.27\n0.15\n0.22\n0.30\n0.33\n0.38"
    assert captured.out == expected_output

def test_with_summary_statistics_decorator(stats: ExecutionTimesBaseStatistics, capsys: CaptureFixture) -> None:
    decorated_func = with_summary_statistics(stats.display_statistics)
    decorated_func()
    captured = capsys.readouterr()
    expected_output = "Count: 5, Sum: 1.38, Min: 0.15, Max: 0.38\n0.15\n0.22\n0.30\n0.33\n0.38"
    assert captured.out == expected_output

def test_with_mean_statistics_decorator_function(stats: ExecutionTimesBaseStatistics, capsys: CaptureFixture) -> None:
    decorated_func = with_mean_statistics(stats.display_statistics)
    decorated_func()
    captured = capsys.readouterr()
    expected_output = "Average results: 0.27\n0.15\n0.22\n0.30\n0.33\n0.38"
    assert captured.out == expected_output

def test_with_summary_statistics_decorator_function(stats: ExecutionTimesBaseStatistics, capsys: CaptureFixture) -> None:
    decorated_func = with_summary_statistics(stats.display_statistics)
    decorated_func()
    captured = capsys.readouterr()
    expected_output = "Count: 5, Sum: 1.38, Min: 0.15, Max: 0.38\n0.15\n0.22\n0.30\n0.33\n0.38"
    assert captured.out == expected_output

def test_abstract_class_instantion() -> None:
    with pytest.raises(TypeError):
        StatisticsLogger()


if __name__ == "__main__":
    pytest.main()

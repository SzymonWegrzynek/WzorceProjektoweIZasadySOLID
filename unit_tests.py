from main import StatisticsLogger, ExecutionTimesBaseStatistics

def test_abstract_class_instantion():
    StatisticsLogger
    assert False


# def test_get_execution_times():
#     execution_times = [0.15, 0.22, 0.30]
#     stats = ExecutionTimesBaseStatistics(execution_times)
#     assert

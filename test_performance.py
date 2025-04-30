import time 
from my_code import long_ruunning_function

def test_long_ruunning_function():
    start_time = time.time()
    long_ruunning_function()
    end_time = time.time()
    duration = end_time - start_time
    assert duration < 3, f"A função demorou {duration}, mais do que o esperad "
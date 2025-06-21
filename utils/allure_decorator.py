import allure
import functools

def allure_step(step_name):
    """
    Decorator to wrap a function within an Allure step for better reporting.

    :param step_name: The name of the step as displayed in Allure reports.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with allure.step(step_name):
                return func(*args, **kwargs)
        return wrapper
    return decorator
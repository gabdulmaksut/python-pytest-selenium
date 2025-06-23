import allure
import functools
import inspect
import string

def allure_step(step_name):
    """
    Decorator to wrap a function within an Allure step for better reporting.
    Supports string formatting with parameter names, e.g. "Do something with {param_name}"

    :param step_name: The name of the step as displayed in Allure reports.
                      Can include {param_name} placeholders that will be replaced with actual values.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Get function parameter names
            sig = inspect.signature(func)
            param_names = list(sig.parameters.keys())

            # Create a dictionary of parameter names and values
            params_dict = {}

            # Add positional arguments (skip 'self' for instance methods)
            start_idx = 1 if param_names and param_names[0] == 'self' else 0
            for i, arg in enumerate(args[start_idx:], start=start_idx):
                if i < len(param_names):
                    params_dict[param_names[i]] = arg

            # Add keyword arguments
            params_dict.update(kwargs)

            # Format the step name with the parameter values
            formatted_step_name = step_name
            try:
                # Use string.Formatter to safely replace placeholders
                if '{' in step_name:
                    formatted_step_name = string.Formatter().vformat(step_name, (), params_dict)
            except (KeyError, ValueError) as e:
                # If formatting fails, use the original step name
                pass

            # Execute the function within an Allure step
            with allure.step(formatted_step_name):
                return func(*args, **kwargs)
        return wrapper
    return decorator
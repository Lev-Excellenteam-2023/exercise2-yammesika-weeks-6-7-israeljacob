import datetime


def timer(func, *args):
    """
    Measures the execution time of a function.

    Parameters:
        func (function): The function to be timed.
        *args: Variable length argument list to be passed to the function.

    Returns:
        datetime.timedelta: The elapsed time for the function execution.
    """
    time = datetime.datetime.now()
    func(args)
    time = datetime.datetime.now() - time
    return time

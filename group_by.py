from typing import Callable, Iterable, Dict, List


def group_by(func: Callable, iterable: Iterable) -> Dict[List]:
    """
    Groups the elements of an iterable based on the results of applying a function to each element.

    Parameters:
        func (function): The function used to determine the grouping key.
        iterable (iterable): The iterable object to be grouped.

    Returns:
        dict: A dictionary with grouping keys as keys and lists of grouped elements as values.
    """
    return {func(item): [iter for iter in iterable if func(item) == func(iter)] for item in iterable}

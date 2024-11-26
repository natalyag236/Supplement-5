def calculate_square_root(number):  
    """Calculates the sqaure root of a given number

    Args:
        number (float): the  number to calculate the sqaure root

    Returns:
        float: the sqaure root of the number 
    """
    return number ** 0.5

def test_calculate_square_root():
    assert calculate_square_root(9) == 3

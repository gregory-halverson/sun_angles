import numpy as np

def day_angle_rad_from_DOY(DOY: np.ndarray) -> np.ndarray:
    """
    Calculate the day angle in radians from the day of the year.

    Parameters:
    DOY (np.ndarray): A numpy array containing day of the year values (integers between 1 and 365).

    Returns:
    np.ndarray: A numpy array containing the corresponding day angles in radians.

    The day angle is calculated using the formula:
    day_angle = (2 * π * (DOY - 1)) / 365
    
    This formula converts the day of the year into an angle in radians, 
    with 0 radians representing the start of the year (DOY=1) and 
    2π radians representing the end of the year (DOY=365).

    Reference:
    Duffie, J. A., & Beckman, W. A. (2013). Solar Engineering of Thermal Processes (4th ed.). Wiley.
    """
    return (2 * np.pi * (DOY - 1)) / 365
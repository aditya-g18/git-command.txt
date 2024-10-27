"""
This module provides functionality to generate a one-time password (OTP).
"""

import random
import string

def generate_otp(length=6):
    """
    Generates an OTP of a specified length.
    
    Args:
        length (int): The length of the OTP to be generated (default is 6).
        
    Returns:
        str: A string representing the generated OTP.
    """
    characters = string.digits
    otp = ''.join(random.choice(characters) for _ in range(length))
    return otp

if __name__ == "__main__":
    print("Your OTP is:", generate_otp())

import pandas as pd
import string

def from_numpy(array):
    """
    Creates a pd.DataFrame from a np.ndarray with capitalized alphabetical column labels.
    
    Args:
        array: np.ndarray, input array to convert
        
    Returns:
        pd.DataFrame with columns labeled A, B, C, ... in alphabetical order
    """
    # Get the number of columns from the array shape
    num_cols = array.shape[1]
    # Generate column labels using uppercase alphabet (A, B, C, ...)
    columns = list(string.ascii_uppercase[:num_cols])
    # Create DataFrame with array data and column labels
    return pd.DataFrame(array, columns=columns)


import numpy as np
def convert_to_ord_arr(dstring):
    return np.array([[ord(x) for x in dstring]])

def annotate_ends(darr):
    """
    
    """
    return np.append(darr, np.array(-1))

def rotate_array(dstring):
    """
    
    """
    out = convert_to_ord_arr(dstring)
    out = annotate_ends(out)
    for i in range(out.size-1):
        row = out[-1] if len(out.shape) > 1 else out
        newrow = np.insert(row[:-1], 0, row[-1])
        out = np.vstack([out, newrow])
    return out

def sort_array(rotated_array):
    """
    Sorts the rotated string in lexiconical order
    Args:
        rotated_array (np.array): A M x N array of integers
    """
    return rotated_array[np.lexsort(np.fliplr(rotated_array).T)]


def final_btw_transform(sorted_arr):
    """
    Returns the last column of a M x N size array. When done on a lexiconically
    sorted arrary, this will be the Burrows-Wheeler Transform
    """
    return sorted_arr[:,-1]

def reverse_bwt_transform(transform):
    """
    Take a BWT integer array and return the string that was used as input to create it
    """
    curr_arr = np.sort(transform)
    for i in range(transform.size-1):
        curr_arr = np.column_stack([transform, curr_arr])
        curr_arr = sort_array(curr_arr)
    return "".join([chr(x) for x in curr_arr[0,1:]])
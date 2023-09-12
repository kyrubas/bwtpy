import numpy as np
def convert_to_ord_arr(dstring):
    """
    Coverts a string of characters to an integer array
    """
    return np.array([[ord(x) for x in dstring]])

def annotate_end(darr):
    """
    Adds a -1 to denote the end of the array
    """
    return np.append(darr, np.array(-1))

def rotate_array(dstring):
    """
    Does the following: 
        Takes in a sequence to convert to ordinal
        Annotates the end of the sequence
        Rotates a copy of the last row by 1 postion
        Stacks array on top of rotated row
    """
    out = convert_to_ord_arr(dstring)
    out = annotate_end(out)
    for i in range(out.size-1):
        newrow = np.roll(out[-1] if len(out.shape) > 1 else out, 1)
        out = np.vstack([out, newrow])
    return out

def sort_array(rotated_array):
    """
    Sorts the an array in lexiconical order
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
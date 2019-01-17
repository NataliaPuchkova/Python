def 
quicksort(sequence):
    """Classic implementation of quicksort using list 
    comprehensions and assuming the traditional relational
    operators work.  The primary weakness of this particular
    implementation of quicksort is that it makes two passes
    over the sequence instead of just one."""
    
    if (len(sequence) == 0): return sequence
    front = quicksort([le for le in sequence[1:] if le <= sequence[0]])
    back = quicksort([gt for gt in sequence[1:] if gt > sequence[0]])
    return front +[sequence[0]] + back

```python
@xl_func("int x, int n, int decimal_places: var")
def stats_X(x, n, decimal_places=3):
    """Return a list of lists counting and comparing number of runs with each possible length

    :param x: integer number of values per run
    :param n: integer number of runs
    :param decimal_places: decimal places in ratio result 

    Returns:
        a 3-column by x-row range
        column 1: possible values of counter function
        column 2: count of runs for each possible value
        column 3: ratio of specific count of runs to total runs, n
        
    Raises:
        "Function error" if function fails

    Example:

        = stats_X(10,50000,3) returns

        0:     47  0.001
        1:    489  0.010
        2:   2224  0.044
        3:   5882  0.118
        4:  10232  0.205
        5:  12299  0.246
        6:  10183  0.204
        7:   5933  0.119
        8:   2135  0.043
        9:    533  0.011
        10:    43  0.001
    """

    try:
        # consider x might be a list or an int
        # this avoids the error from len(an_integer)
        len_int_or_list = lambda x: 0 if x == 0 else len(x)

        results = []
        # note: next line is continued
        results = [len_int_or_list(filter_int_comp_list_X(0.5, 1.0, 'oo', mix_func(x))) \
                   for e in range(n)]
        
        counts = Counter(results)
        
        output = []
        # collect all the counts and ratios into a list of lists
        for e in range(x+1):
            output.append([str(e)+':', counts.get(e, 0), KLHfloatround(counts.get(e, 0)/n,decimal_places)])
        return output
    except:
        return 'Function error'
```

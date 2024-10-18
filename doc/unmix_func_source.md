---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

```python
from random import random
@xl_func("object x: var")
def unmix_func(x):
    """Return a list of lists

    Args:
        x: a 1-dimensional list object
        
    Returns:
        a list of lists (suitable for PyXLL) 
        
    Raises:
        "empty" if function fails
    """
    try:
        return [[e] for e in x]
    except:
        return 'empty'
```

```{code-cell} ipython3
:tags: [hide-output, show-input]

# from myst_nb import glue
import myst_nb as mnb

a = "KLH"
mnb.glue("my_variable_a", a, display=False)
b = 3.1416
mnb.glue("my_variable_b", b, display=False)
```

```{glue:} my_variable
```

```{code-cell} ipython3
:tags: [hide-input]
from myst_nb import glue
import myst_nb as mnb
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 200)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y, 'b-', linewidth=2)

fig.set_size_inches(0.5, 0.166)
fig.set_facecolor('white')
fig.set_edgecolor('white')

ax.set_xticks([])
ax.set_yticks([])
ax.set_axis_off()

mnb.glue("glued_fig_b", fig, display=False)

temp = ''
```

```{code-cell} ipython3
:tags: [hide-output, hide-input]
from myst_nb import glue
import myst_nb as mnb
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 200)
y = np.cos(x)
fig, ax = plt.subplots()
ax.plot(x, y, 'r-', linewidth=2)

fig.set_size_inches(0.5, 0.166)
fig.set_facecolor('white')
fig.set_edgecolor('white')

ax.set_xticks([])
ax.set_yticks([])
ax.set_axis_off()

mnb.glue("glued_fig_r", fig, display=False)

temp = ''
```

```{glue:figure} glued_fig_b
```

```{glue:} my_variable_a
```

```{glue:} my_variable_b
```

Inline (1a) txt {glue:}`my_variable_a`, and fig {glue:}`glued_fig_b`.

Inline (1b) txt {glue:}`my_variable_b`, and fig {glue:}`glued_fig_r`.

```{code-cell} ipython3
:tags: [hide-output, hide-input]
import itertools
from collections import Counter
from random import random
from decimal import *
from numbers import Number

def KLHfloatround(myfloat, my10power):
    return float(
        Decimal(round(myfloat, my10power)).quantize(Decimal(str(10**-my10power)))
    )

def interval_compare_X(bracket_number1, bracket_number2, interval_type):
    """Given an Excel cell, filter the numeric value, retaining only if within the interval

    Args:
        bracket_number1: one extreme value in the interval (*)
        bracket_number2: the other extreme value in the interval (*)
        interval_type: type of interval closure (closed/open and combinations)
        number_entry: a single Excel cell to be filtered
        sortQ: a boolean, True indicates an ascending sort
        reverseQ: a boolean, True indicates sorted descending
        unique_onlyQ: a boolean, indicates removal of duplicates
        (*) or in ["minf", "pinf", "-inf", "inf"]

    Returns:
        List of values meeting the comparison specification, if any. Otherwise, the string 'empty'
        
    Raises:
        ValueError("Expected 2 numeric values and string interval_type")

    """
    b1, b2 = min(bracket_number1, bracket_number2), max(bracket_number1, bracket_number2)

    b1_ok, b2_ok = False, False
    
    if isinstance(b1, str):
        b1 = bracket_inf(b1)
        if not b1:
            input_check = False
            # print("ValueError('bracket1 must be numeric")
            raise ValueError('bracket1 must be numeric or in ["minf", "pinf", "-inf", "inf"]')
        else:
            b1_ok =True

    if isinstance(b2, str):
        b2 = bracket_inf(b2)
        if not b2:
            # print("ValueError('bracket2 must be numeric")
            raise ValueError('bracket2 must be numeric or in ["minf", "pinf", "-inf", "inf"]')
        else:
            b2_ok =True
    
    if not ((isinstance(b1, Number) or b1_ok) 
            and (isinstance(b2, Number) or b2_ok) 
            and isinstance(interval_type, str)):
        # print("ValueError('Expected ...")
        raise ValueError("Expected 2 numeric values (*) and string interval_type")

    ivupper = interval_type.upper()

    if not(ivupper in ['[]','[)','(]','()','CC','CO','OC','OO']):
        raise ValueError("Interval_type must be \n['[]','[)','(]','()','CC','CO','OC','OO']")
                                   
    if ivupper in ['[]','CC']:
        def CC(x):
            if (b1 < x < b2):
                return x
            else:
                return None
        return CC
    elif ivupper in ['[)','CO']:
        def CO(x):
            if (b1 < x <= b2):
                return x
            else:
                return None
        return CO
    elif ivupper in ['(]','OC']:
        def OC(x):
            if (b1 <= x < b2):
                return x
            else:
                return None
        return OC
    elif ivupper in ['()','OO']:
        def OO(x):
            if (b1 <= x <= b2):
                return x
            else:
                return None
        return OO

def interval_compare_X(bracket_number1, bracket_number2, interval_type):
    """Given an Excel cell, filter the numeric value, retaining only if within the interval

    Args:
        bracket_number1: one extreme value in the interval (*)
        bracket_number2: the other extreme value in the interval (*)
        interval_type: type of interval closure (closed/open and combinations)
        number_entry: a single Excel cell to be filtered
        sortQ: a boolean, True indicates an ascending sort
        reverseQ: a boolean, True indicates sorted descending
        unique_onlyQ: a boolean, indicates removal of duplicates
        (*) or in ["minf", "pinf", "-inf", "inf"]

    Returns:
        List of values meeting the comparison specification, if any. Otherwise, the string 'empty'
        
    Raises:
        ValueError("Expected 2 numeric values and string interval_type")

    """
    b1, b2 = min(bracket_number1, bracket_number2), max(bracket_number1, bracket_number2)

    b1_ok, b2_ok = False, False
    
    if isinstance(b1, str):
        b1 = bracket_inf(b1)
        if not b1:
            input_check = False
            # print("ValueError('bracket1 must be numeric")
            raise ValueError('bracket1 must be numeric or in ["minf", "pinf", "-inf", "inf"]')
        else:
            b1_ok =True

    if isinstance(b2, str):
        b2 = bracket_inf(b2)
        if not b2:
            # print("ValueError('bracket2 must be numeric")
            raise ValueError('bracket2 must be numeric or in ["minf", "pinf", "-inf", "inf"]')
        else:
            b2_ok =True
    
    if not ((isinstance(b1, Number) or b1_ok) 
            and (isinstance(b2, Number) or b2_ok) 
            and isinstance(interval_type, str)):
        # print("ValueError('Expected ...")
        raise ValueError("Expected 2 numeric values (*) and string interval_type")

    ivupper = interval_type.upper()

    if not(ivupper in ['[]','[)','(]','()','CC','CO','OC','OO']):
        raise ValueError("Interval_type must be \n['[]','[)','(]','()','CC','CO','OC','OO']")
                                   
    if ivupper in ['[]','CC']:
        def CC(x):
            if (b1 < x < b2):
                return x
            else:
                return None
        return CC
    elif ivupper in ['[)','CO']:
        def CO(x):
            if (b1 < x <= b2):
                return x
            else:
                return None
        return CO
    elif ivupper in ['(]','OC']:
        def OC(x):
            if (b1 <= x < b2):
                return x
            else:
                return None
        return OC
    elif ivupper in ['()','OO']:
        def OO(x):
            if (b1 <= x <= b2):
                return x
            else:
                return None
        return OO
    
def filter_int_comp_list_X(bracket_number1, bracket_number2, interval_type, number_entry_list, sortQ=False, reverseQ=False, unique_onlyQ=False):
    """Given an Excel range, filter the numeric values, retaining only those that are within the interval

    Args:
        bracket_number1: one extreme value in the interval
        bracket_number2: the other extreme value in the interval
        interval_type: type of interval closure (closed/open and combinations)
        number_entry_list: a LIST of values to be filtered
        sortQ: a boolean, True indicates sorted ascending
        reverseQ: a boolean, True indicates sorted descending
        unique_onlyQ: a boolean, indicates removal of duplicates

    Returns:
        List of values meeting the comparison specification, if any. Otherwise, the string 'empty'
        
    Raises:
        string 'Error in multiple range input': If the function fails.

    """

    ret = []
    icx=interval_compare_X(bracket_number1, bracket_number2, interval_type)
    # rg_flattened = itertools.chain.from_iterable(number_entry_range)
    # for e in number_entry_list:
    #     e_value = None
    #     if e == '' or e is None:
    #         # no conversion
    #         e_value = ''
    #     else:
    #         try:
    #             e_value = e.Value
    #         except:
    #             e_value = e
    #     if type(e_value) == float:
    #         comparison = icx(e_value)
    #         if comparison:
    #             ret.append(e_value)

    # ret = [icx(x) for x in number_entry_list]       

    ret = [y for x in number_entry_list for y in [icx(x)] if y is not None]

    if unique_onlyQ:
        ret = list(set(ret))
    if sortQ:
        ret.sort()
    if reverseQ:
        ret.reverse()

    if len(ret) == 0:
        return 0
    else:
        return ret
    
def mix_func(x):
    """Return a list of x random values

    Args:
        x: integer number of values to produce
        
    Returns:
        an x-length list of random numbers
        
    Raises:
        zero, if x == 0
        "Function error" if function fails

    Disclosure:
        Lifted from Page 56 of https://www.pyxll.com/docs/pyxll-5.5.4.pdf         
    """
    try:
        if x == 0:
            # return as a number to Excel
            return 0

        # return a list of values as an 'object'
        array = [random() for i in range(x)]
        return array
    except:
        return "Function error"

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

        0:	47     0.001
        1:	489    0.010
        2:	2224   0.044
        3:	5882   0.118
        4:	10232  0.205
        5:	12299  0.246
        6:	10183  0.204
        7:	5933   0.119
        8:	2135   0.043
        9:	533    0.011
        10:	43     0.001
    """

    try:
        # consider x might be a list or an int
        # this avoids the error from len(an_integer)
        len_int_or_list = lambda x: 0 if x == 0 else len(x)
        results = []
        # for f in range(n):
        #     mfx = mix_func(x)
        #     this_run = filter_int_comp_list(0.0, 0.5, 'oo', mfx)
        #     results.append(len_int_or_list(this_run))
        results = [len_int_or_list(filter_int_comp_list_X(0.5, 1.0, 'oo', mix_func(x))) \
                   for e in range(n)]
        
        counts = Counter(results)
        output = []
        # total = sum([counts.get(e, 0) for e in counts])
        for e in range(x+1):
            output.append([str(e)+':', counts.get(e, 0), KLHfloatround(counts.get(e, 0)/n,decimal_places)])
        return output
    except:
        return 'Function error'

# temp2 = mix_func(10)

# temp3 = KLHfloatround(myfloat, my10power)

temp = stats_X(10,500,3)

qout = temp[5,1]
```

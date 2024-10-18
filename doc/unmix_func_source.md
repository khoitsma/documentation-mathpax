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
:tags: [hide-output, hide-input]
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
from collections import Counter

from random import random
# @xl_func("int x: object<skip_primitives=True>")
@xl_func("int x: object")
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
    """Return a list of lists couting and comparing number of runs with each possible length

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

        0:	47	    0.001
        1:	489	    0.010
        2:	2224	0.044
        3:	5882	0.118
        4:	10232	0.205
        5:	12299	0.246
        6:	10183	0.204
        7:	5933	0.119
        8:	2135	0.043
        9:	533	    0.011
        10:	43	    0.001

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

temp = stats_X(10,5000,3)
```

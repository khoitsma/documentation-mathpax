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
# from myst_nb import glue
import myst_nb as mnb
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 200)
y = np.sin(x)
fig, ax = plt.subplots()
fig.set_size_inches(6, 2)
ax.plot(x, y, 'b-', linewidth=2)
mnb.glue("glued_fig", fig, display=False)
temp = ''
```

```{glue:figure} glued_fig
```

```{glue:} my_variable_a
```

```{glue:} my_variable_b
```

Inline (1a) txt {glue:}`my_variable_a`, and fig {glue:}`glued_fig`.

Inline (1b) txt {glue:}`my_variable_b`, and fig {glue:}`glued_fig`.

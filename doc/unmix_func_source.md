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

from myst_nb import glue
a = "KLH my variable!"
glue("my_variable", a)
```

```
{glue} `my_variable`
```

```{code-cell} ipython3
:tags: [hide-output, show-input]

from myst_nb import glue
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 200)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y, 'b-', linewidth=2)
glue("glued_fig", fig, display=False)
```

```
This is an inline glue example of a figure: {glue:figure} `glued_fig`.
```

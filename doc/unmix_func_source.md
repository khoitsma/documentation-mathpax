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

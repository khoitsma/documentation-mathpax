```python
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
```

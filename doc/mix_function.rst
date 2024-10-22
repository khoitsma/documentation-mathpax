.. role:: raw-html(raw)
    :format: html

mix_func
========

An example function to provide a list of x random values 

Args:

:x: integer number of values to produce
        
Returns:

 | an x-length list of random numbers
        
Raises:

 | zero, if x == 0
 | "Function error" if function fails

Disclosure:

 | Lifted from Page 56 of https://www.pyxll.com/docs/pyxll-5.5.4.pdf         

.. include:: mix_func_source.md
   :parser: myst_parser.sphinx_

.. plotly::

   import plotly.express as px

   px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])

.. plotly:: 

   :iframe-width: 500px
   :iframe-height: 300px

   import plotly.express as px

   px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])

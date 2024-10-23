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

% Plotly doesn't work with Sphinx
.. plotly::
   :iframe-width: 500px
   :iframe-height: 300px

   import plotly.express as px
   fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])
   fig.write_html('first_figure.html', auto_open=True)

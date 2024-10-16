.. role:: raw-html(raw)
    :format: html

Interval_Filter
===============

An example statistical function using Python and PyXLL_

.. _PyXLL: https://www.pyxll.com
.. _Write to me: jdoe@example.com
      
.. epigraph::

 | What is the probability that you will have

 | ... exactly 7 heads out of a total of 10 coin tosses?       
 | ... or exactly 14 heads out of a total of 20 coin tosses?     

Return a list of lists **counting** and **comparing the number** of runs with each possible length

:x: integer number of values per run
:n: integer number of runs
:decimal_places: decimal places in ratio result 

Returns:

 | an Excel range (3 columns by x+1 rows)
 | column 1 — all possible values of counter function (0 to x)
 | column 2 — count of runs for each possible value
 | column 3 — ratio of each specific count of runs to total runs, n
 
Raises:
"Function error" if the function fails

Example::

 stats_X(10, 50000, 3) 

returns

.. include:: include_note.md
   :parser: myst_parser.sphinx_

.. include:: statsX_func_source.md
   :parser: myst_parser.sphinx_

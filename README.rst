===========================================
Scientific coding workshop: Twitter dataset
===========================================

This dataset contains agrregation infromation over tweets about London Olympics,
Koninginnedag (a Dutch national holiday) in 2012, Pinkpop 2012 and the UEFA Euro
2012 fotball tournament.

Data
====

Timeline
--------

``koninginnedag.txt``, ``olympics.txt``, ``pinkpop.txt`` and ``uefa_euro.txt``
contain information of amount of tweets being written per hour for the
correspondng events. You can plot it using ``gnuplot`` and the ``timeline.dat``
script and see the resutl in ``timeline.pdf``:

.. code-block:: bash

    gnuplot timeline.dat

The timeline (``*.txt``) files contain two columns separated by space:

.. code-block:: bash

    head olympics.txt
    2012-08-11-00 13350
    2012-08-11-01 12777
    2012-08-11-02 14249
    2012-08-11-03 15746
    2012-08-11-04 9104
    2012-08-11-05 9262
    2012-08-11-06 9056
    2012-08-11-07 10495
    2012-08-11-08 15119
    2012-08-11-09 18497

where the first column is the hour and the second is the number of thweets
collected.

Reply
-----

The ``*__reply.csv.gz`` files are comma separated file with 3 columns separated by
comma and space:

* the time a tweet was created
* the id of the tweet
* the id of a tweet this tweet is reply to, ``None`` otherwise.

Here is a short sample::

  2012-08-11 00:01:58, 234077159721943040, None
  2012-08-11 00:01:58, 234077159453499393, 234071638377889792
  2012-08-11 00:01:58, 234077161231888384, None
  2012-08-11 00:01:58, 234077160770514944, None
  2012-08-11 00:01:59, 234077162729242624, 233155831913390080

Tasks
=====

1. Write a script that generates an timeline plot for a collection of tweets.

   * The script should take the name of an input file (e.g. ``olympics.txt``) as
     a positional argument.

   * The  generated plot should be stored in file with a name passed using an
     optional argument ``--output`` (e.g. ``--output olympics.png``)

   * It should be possible run the script using the following command::

      timeline.py olympics.txt --output olympics.png

   Modify the ``timeline()`` function in ``timeline.py`` to generate the plots.


2. Write a script that given a ``*_reply.csv.gz`` file plots the distribution of
   differences of the ID of a tweet and the tweet's ID it's a reply to.


You might want to use `Pandas`_ for data processing and plotting, and `opster`_
for handling command line arguments. Opster is available in this repo as
``opster.py``. Refer to the Overview__ section of the opster docs to see how
options are defined.


.. _Pandas: http://pandas.pydata.org/pandas-docs/stable/
.. _opster: http://opster.readthedocs.org/

__ http://opster.readthedocs.org/en/latest/overview.html

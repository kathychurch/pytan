
Ask Manual Question Sensor With Parameters And Filter And Options
========================================================================================

Ask a manual question using human strings by referencing the name of a single sensor that takes parameters, but supplying only two of the four parameters that are used by the sensor.

Also supply a sensor filter that limits the column data that is shown to values that match the regex '.*Shared.*', and a sensor filter option that re-fetches any cached data that is older than 3600 seconds.

No question filters or question options supplied.


* `STDOUT from Example Python Code <../_static/pytan_outputs/ask_manual_question_sensor_with_parameters_and_filter_and_options_stdout.txt>`_
* `STDERR from Example Python Code <../_static/pytan_outputs/ask_manual_question_sensor_with_parameters_and_filter_and_options_stderr.txt>`_
* Example Python Code

.. literalinclude:: ask_manual_question_sensor_with_parameters_and_filter_and_options_code.py
    :linenos:
    :language: python

.. rubric:: Footnotes

.. [#] this file automatically created by BUILD/build_api_examples.py

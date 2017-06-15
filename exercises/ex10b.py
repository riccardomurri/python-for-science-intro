#! /usr/bin/python
#
"""
Exercise 10.B:

Edit the ``ex10a.py`` file: insert the code to define the
``PricingApp1`` application, and modify the ``new_tasks()``
method to return one instance of it (as in the previous
slide).

Can you process the ``simAsset1.dat`` file using this GC3Pie
script?
"""

from gc3libs.cmdline \
  import SessionBasedScript


if __name__ == '__main__':
  # whenever the file is renamed, also
  # the two lines below MIST change accordingly
  import ex10b
  ex10b.AScript().run()


# no need to copy+paste code here! just download `pricingapp1.py` from the
# `download/` directory of the course and use it as a module
from pricingapp1 import PricingApp1


class AScript(SessionBasedScript):
  """
  Run `simAsset.R` on each given input file.
  """
  def __init__(self):
    super(AScript, self).__init__(
        version='1.0')
  def new_tasks(self, extra):
    try:
      # allow name of input file to be given on the command-line
      input_file = self.params.args[0]
      # run one application per input file
      apps_to_run = [
          PricingApp1(input_file)
      ]
    except IndexError:  # no input file on cmd line
      apps_to_run = [ ]
    return apps_to_run

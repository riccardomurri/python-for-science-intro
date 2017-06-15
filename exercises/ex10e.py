#! /usr/bin/python
#
"""
Exercise 10.E:

Edit the script from Exercise 10.B and add the ability to process multiple
input files: for each file name given on the command line, an instance of
``ProcessingApp1`` should be run.
"""

from gc3libs.cmdline \
  import SessionBasedScript


if __name__ == '__main__':
  # whenever the file is renamed, also
  # the two lines below MIST change accordingly
  import ex10e
  ex10e.AScript().run()


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
    apps_to_run = [ ]
    for input_file in self.params.args:
      # run one application per input file
      apps_to_run.append(PricingApp1(input_file))
    return apps_to_run

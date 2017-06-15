import os
from os.path import basename

from gc3libs import Application


class PricingApp1(Application):
  """Simulate asset pricing."""
  def __init__(self, infile):
    inp = basename(infile)
    Application.__init__(
      self,
      arguments=[
        'Rscript', 'simAsset.R', inp],
      inputs=['simAsset.R', infile],
      outputs=['result1.csv', 'result1.pdf'],
      output_dir='pricing1.d',
      stdout='stdout.txt')

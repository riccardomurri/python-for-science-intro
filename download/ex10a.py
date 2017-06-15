from gc3libs.cmdline \
  import SessionBasedScript

if __name__ == '__main__':
  import ex10a
  ex10a.AScript().run()

class AScript(SessionBasedScript):
  """
  Minimal workflow scaffolding.
  """
  def __init__(self):
    super(AScript, self).__init__(
        version='1.0')
  def new_tasks(self, extra):
    apps_to_run = [ ]
    return apps_to_run

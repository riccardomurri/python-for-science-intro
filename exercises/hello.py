#
# Sample Python module
#

# A Python module is just a file containing Python commands.
# Although *any* Python statement is permitted in a module file,
# only constants, functions, and class definitions should
# normally appear in a Python module file.

def greet(name):
  """A friendly function."""
  print("Hello, " + name + "!")
  
# the following is just for demo purposes during the course,
# it should not appear in a real module (see above).
import sys
print("Greetings from `hello.py`", file=sys.stderr)
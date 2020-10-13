#!/usr/bin/env python
import os
import sys
import unittest


suite = unittest.TestLoader().discover(start_dir="./test",  pattern="test*.py")

runner = unittest.TextTestRunner(verbosity=3)
tr = runner.run(suite)
sys.exit(len(tr.errors)  +  len(tr.failures))

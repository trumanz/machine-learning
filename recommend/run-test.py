#!/usr/bin/env python

import unittest


suite = unittest.TestLoader().discover(start_dir="./test",  pattern="test*.py")

runner = unittest.TextTestRunner(verbosity=3)
runner.run(suite)

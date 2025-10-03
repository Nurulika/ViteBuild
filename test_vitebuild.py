# test_vitebuild.py
"""
Tests for ViteBuild module.
"""

import unittest
from vitebuild import ViteBuild

class TestViteBuild(unittest.TestCase):
    """Test cases for ViteBuild class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ViteBuild()
        self.assertIsInstance(instance, ViteBuild)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ViteBuild()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

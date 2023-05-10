import unittest
import importlib.util
import air00

# Class 
class TestScript(unittest.TestCase):
    script_path = "air00.py"
    # To test if present
    def test_script_present(self):
        self.assertTrue(importlib.util.find_spec('air00'))
    # To test if runs
    def test_script_runs(self):
        try:
            self.assertEqual(air00.separation('Bonjour les gars', [' ']), ['onjour', 'les', 'gars'])
        except Exception as e:
            self.fail(f"Le script '{self.script_path}' a rencontré une erreur lors de l'éxecution : {e}")

# Principal main
if __name__ == '__main__':
    unittest.main()

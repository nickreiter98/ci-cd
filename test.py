import unittest
import pandas as pd
from exec.run import get_data_set, store_scatter_plot

class TestDataSet(unittest.TestCase):
    def test_get_data_set(self):
        df = get_data_set()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (150, 5))

if __name__ == '__main__':
    unittest.main()
import unittest
from customer_behavior.data_processing import load_data, clean_data, preprocess_data

class TestDataProcessing(unittest.TestCase):

    def test_load_data(self):
        # Test loading data from a file
        data = load_data('data/raw/sample_data.csv')
        self.assertIsNotNone(data)
        self.assertGreater(len(data), 0)

    def test_clean_data(self):
        # Test cleaning data
        raw_data = {'column1': [1, 2, None], 'column2': ['A', 'B', 'C']}
        cleaned_data = clean_data(raw_data)
        self.assertNotIn(None, cleaned_data['column1'])
        self.assertEqual(len(cleaned_data['column2']), 3)

    def test_preprocess_data(self):
        # Test preprocessing data
        raw_data = {'column1': [1, 2, 3], 'column2': ['A', 'B', 'C']}
        processed_data = preprocess_data(raw_data)
        self.assertIn('processed_column', processed_data.columns)

if __name__ == '__main__':
    unittest.main()
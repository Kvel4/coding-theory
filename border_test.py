import unittest

from border import gr_find_k_by_n_d, gr_find_d_by_n_k, vg_find_d_by_n_k, vg_find_k_by_n_d, hamming_find_d_by_n_k, hamming_find_k_by_n_d


class BorderTest(unittest.TestCase):
    def test_hamming_n_k_17_8(self):
        self.assertEqual(7, hamming_find_d_by_n_k(17, 8))

    def test_vg_n_k_17_8(self):
        self.assertEqual(4, vg_find_d_by_n_k(17, 8))

    def test_gr_n_k_17_8(self):
        self.assertEqual(6, gr_find_d_by_n_k(17, 8))

    def test_vg_n_d_20_10(self):
        self.assertEqual(2, vg_find_k_by_n_d(20, 10))

    def test_hamming_n_d_20_10(self):
        self.assertEqual(7, hamming_find_k_by_n_d(20, 10))

    def test_gr_n_d_20_10(self):
        self.assertEqual(4, gr_find_k_by_n_d(20, 10))

    def test_hamming_n_k_14_6(self):
        self.assertEqual(7, hamming_find_d_by_n_k(14, 6))

    def test_gr_n_k_14_6(self):
        self.assertEqual(6, gr_find_d_by_n_k(14, 6))

    def test_vg_n_k_14_6(self):
        self.assertEqual(4, vg_find_d_by_n_k(14, 6))

    def test_hamming_n_d_16_5(self):
        self.assertEqual(8, hamming_find_k_by_n_d(16, 5))

    def test_gr_n_d_16_5(self):
        self.assertEqual(9, gr_find_k_by_n_d(16, 5))

    def test_vg_n_d_16_5(self):
        self.assertEqual(6, vg_find_k_by_n_d(16, 5))

    def test_hamming_n_k_17_10(self):
        self.assertEqual(5, hamming_find_d_by_n_k(17, 10))

    def test_gr_n_k_17_10(self):
        self.assertEqual(5, gr_find_d_by_n_k(17, 10))

    def test_vg_n_k_17_10(self):
        self.assertEqual(3, vg_find_d_by_n_k(17, 10))

    def test_hamming_n_d_15_7(self):
        self.assertEqual(5, hamming_find_k_by_n_d(15, 7))

    def test_gr_n_d_15_7(self):
        self.assertEqual(5, gr_find_k_by_n_d(15, 7))

    def test_vg_n_d_15_7(self):
        self.assertEqual(3, vg_find_k_by_n_d(15, 7))

    def test_hamming_n_k_12_8(self):
        self.assertEqual(3, hamming_find_d_by_n_k(12, 8))

    def test_gr_n_k_12_8(self):
        self.assertEqual(4, gr_find_d_by_n_k(12, 8))

    def test_vg_n_k_12_8(self):
        self.assertEqual(3, vg_find_d_by_n_k(12, 8))

    def test_hamming_n_d_16_8(self):
        self.assertEqual(6, hamming_find_k_by_n_d(16, 8))

    def test_gr_n_d_16_8(self):
        self.assertEqual(5, gr_find_k_by_n_d(16, 8))

    def test_vg_n_d_16_8(self):
        self.assertEqual(2, vg_find_k_by_n_d(16, 8))

    def test_hamming_n_d_13_6(self):
        self.assertEqual(6, hamming_find_k_by_n_d(13, 6))

    def test_gr_n_d_13_6(self):
        self.assertEqual(5, gr_find_k_by_n_d(13, 6))

    def test_hamming_n_k_12_5(self):
        self.assertEqual(5, hamming_find_d_by_n_k(12, 5))

    # def test_gr_n_k_12_5(self):
    #     self.assertEqual(4, gr_find_d_by_n_k(12, 5))

    def test_hamming_n_d_18_3(self):
        self.assertEqual(13, hamming_find_k_by_n_d(18, 3))

    def test_gr_n_d_18_3(self):
        self.assertEqual(13, gr_find_k_by_n_d(18, 3))

    def test_vg_n_k_18_4(self):
        self.assertEqual(10, vg_find_d_by_n_k(18, 4))

    def test_vg_n_d_17_4(self):
        self.assertEqual(7, vg_find_k_by_n_d(17, 4))

    def test_hamming_n_d_17_4(self):
        self.assertEqual(11, hamming_find_k_by_n_d(17, 4))

    def test_vg_n_k_17_6(self):
        self.assertEqual(5, vg_find_d_by_n_k(17, 6))

    def test_vg_n_d_12_4(self):
        self.assertEqual(5, vg_find_k_by_n_d(12, 4))

    def test_hamming_n_d_12_4(self):
        self.assertEqual(7, hamming_find_k_by_n_d(12, 4))

    # def test_hamming_n_k_12_5(self):
    #         self.assertEqual(5, hamming_find_d_by_n_k(12, 5))

    # def test_gr_n_k_12_5(self):
    #     self.assertEqual(5, gr_find_d_by_n_k(12, 5))

    # def test_vg_n_k_12_5(self):
    #     self.assertEqual(4, vg_find_d_by_n_k(12, 5))

    def test_hamming_n_d_19_3(self):
        self.assertEqual(14, hamming_find_k_by_n_d(19, 3))

    def test_gr_n_d_19_3(self):
        self.assertEqual(16, gr_find_k_by_n_d(19, 3))

    def test_vg_n_d_19_3(self):
        self.assertEqual(14, vg_find_k_by_n_d(19, 3))

    def test_hamming_n_k_19_5(self):
        self.assertEqual(11, hamming_find_d_by_n_k(19, 5))

    def test_gr_n_k_19_5(self):
        self.assertEqual(8, gr_find_d_by_n_k(19, 5))

    def test_vg_n_k_19_5(self):
        self.assertEqual(7, vg_find_d_by_n_k(19, 5))

    def test_hamming_n_d_12_5(self):
        self.assertEqual(5, hamming_find_k_by_n_d(12, 5))

    def test_gr_n_d_12_5(self):
        self.assertEqual(5, gr_find_k_by_n_d(12, 5))

    def test_vg_n_d_12_5(self):
        self.assertEqual(4, vg_find_k_by_n_d(12, 5))


if __name__ == '__main__':
    unittest.main()

import unittest

def mow_lawn(raining):
    if raining == True:
        return False
    elif raining == False:
        return True

def cover_track(raining):
    if raining == True:
        return True
    elif raining == False:
        return False

class TestWorkMethods(unittest.TestCase):

    def test_mow_lawn(self):
        raining = False
        self.assertTrue(mow_lawn(raining))
        raining = True
        self.assertFalse(mow_lawn(raining))

    def test_cover_track(self):
        raining = False
        self.assertFalse(cover_track(raining))
        raining = True
        self.assertTrue(cover_track(raining))

if __name__ == '__main__':
    unittest.main()

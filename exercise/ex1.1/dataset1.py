import unittest
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
font_path = '/Library/Fonts/Arial Unicode.ttf'
font_prop = font_manager.FontProperties(fname = font_path)
matplotlib.rcParams['font.family'] = font_prop.get_name()

def true_function(x):
    x = np.array(x)
    return np.sin(np.pi * x * 0.8) * 10


class TestTrueFunction(unittest.TestCase):
    def test_x_zero_returns_zero(self):
        y = true_function(0)
        np.testing.assert_equal(y, 0)


x = np.linspace(-1, 1)
y = true_function(x)

plt.plot(x, y, label="真の関数")
plt.legend()
plt.savefig("ex1.1.png")
plt.close()


if __name__ == "__main__":
    unittest.main()


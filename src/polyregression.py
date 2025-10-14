import numpy as np

class Polyregression:
    def polyRegression(self, x: list[float], y: list[float]):
        if len(x) != len(y):
            print("Input vectors must have the same length.")
            return

        x = np.array(x)
        y = np.array(y)
        n = len(x)

        xm = np.mean(x)
        ym = np.mean(y)
        x2m = np.mean(x**2)
        x3m = np.mean(x**3)
        x4m = np.mean(x**4)

        xym = np.mean(x * y)
        x2ym = np.mean(x**2 * y)

        sxx = x2m - xm * xm
        sxy = xym - xm * ym
        sxx2 = x3m - xm * x2m
        sx2x2 = x4m - x2m * x2m
        sx2y = x2ym - x2m * ym

        denominator = sxx * sx2x2 - sxx2 * sxx2
        if denominator == 0:
            print("Denominator is zero, can't compute coefficients.")
            return

        b = (sxy * sx2x2 - sx2y * sxx2) / denominator
        c = (sx2y * sxx - sxy * sxx2) / denominator
        a = ym - b * xm - c * x2m

        print(f"y = {a:.6f} + {b:.6f}x + {c:.6f}x^2")

        # Optional: show table of values
        # print("\n x   y     y_pred")
        # for xi, yi in zip(x, y):
        #     y_pred = a + b * xi + c * xi**2
        #     print(f"{xi:.2f}  {yi:.2f}  {y_pred:.2f}")

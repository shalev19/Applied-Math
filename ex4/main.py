import fourierCompSynthesis as fcs




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cn = '(1 / (2 * np.pi)) * (((1 - ((-1)**n) * np.exp(-np.pi)) / (1 - 1j * n)) + ((1 - ((-1)**n) * np.exp(-np.pi)) / (1 + 1.j * n)))'
    func = 'np.exp(-np.abs(x))'
    m = 50
    N = 1000
    y = fcs.FourierCompSynthesis(cn, func, m, N)

    cn = '(((-1)**n) * (np.exp(np.pi) - np.exp(-np.pi))) / (2 * np.pi * (1 - 1.j*n))'
    func1 = '(np.exp(x))'
    m = 50
    N = 1000
    y = fcs.FourierCompSynthesis(cn, func1, m, N)

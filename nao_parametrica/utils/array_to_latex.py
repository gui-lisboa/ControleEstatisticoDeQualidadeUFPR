import numpy as np

def array_to_latex(array: np.array, prefix: str) -> str:
    if len(array.shape) > 2:
        raise ValueError('bmatrix can at most display two dimensions')
    lines = str(array).replace('[', '').replace(']', '').splitlines()
    rv = [r'{0}'.format(prefix)]
    rv += [r'\begin{bmatrix}']
    rv += ['  ' + ' & '.join(l.split()) + r'\\' for l in lines]
    rv += [r'\end{bmatrix}']
    return '\n'.join(rv)
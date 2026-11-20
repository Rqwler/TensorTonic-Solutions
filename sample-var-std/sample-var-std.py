import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    x=np.asarray(x,dtype=float)
    center=x-np.mean(x)
    variance=float(np.sum(center**2))/(x.size-1)
    std_dev=float(np.sqrt(variance))

    return {"variance":variance,"standard_deviation":std_dev}
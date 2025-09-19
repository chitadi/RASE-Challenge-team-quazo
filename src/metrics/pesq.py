
from pesq import pesq as pesq_fn

def nbpesq(target, est_target, fs=8000):
    # y = audios["target"]
    # y_hat = audios["est_target"]

    return pesq_fn(fs, target, est_target, 'nb')


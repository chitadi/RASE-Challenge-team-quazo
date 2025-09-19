
from pystoi.stoi import stoi
def estoi(target, est_target, fs=8000):
    """The extended short-time objective intelligibility (ESTOI)

    Using implementation from https://github.com/mpariente/pystoi

    Parameters
    ----------
    audios : :obj:`dict` of :obj:`numpy.ndarrays`
       Contain keys and time-domain signal pair for "target" and "est_target"

    sampling_rate : int, optional
       The sampling rate of the time-domain signal, by default 16000

    Returns
    -------
    float
        ESTOI result

    References
    ------------
    J. Jensen and C. H. Taal, “An algorithm for predicting the intelligibility of  speech  masked  by  modulated  noise  maskers,”IEEE/ACM Trans.Audio, Speech, Lang. Process.,  vol.  24,  no.  11,  pp.  2009–2022,  Nov.2016.
    """
    # target = audios["target"]
    # est_target = audios["est_target"]
    assert len(est_target.shape) == len(est_target.shape) == 1
    return stoi(target, est_target, fs, extended=True)

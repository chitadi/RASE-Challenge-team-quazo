# from DNSMOS import dnsmos_


import os
from .DNSMOS.dnsmos_local import ComputeScoreFromArray
import requests
from .DNSMOS.dnsmos import SCORING_URI_DNSMOS_P835, SCORING_URI_DNSMOS
p808_model_path = 'metrics/DNSMOS/DNSMOS/model_v8.onnx'
primary_model_path = os.path.join('metrics','DNSMOS', 'DNSMOS', 'sig_bak_ovr.onnx')
compute_score = ComputeScoreFromArray(primary_model_path, p808_model_path)

SAMPLING_RATE=8000


def DNSMOS_BAK(est_target, **kwargs):

    assert len(est_target.shape) == 1

    score_dict = compute_score(est_target, SAMPLING_RATE, is_personalized_MOS=False)

    return score_dict["BAK"]

def DNSMOS_SIG(est_target, **kwargs):


    assert len(est_target.shape) == 1
    
    
    score_dict = compute_score(est_target, SAMPLING_RATE, is_personalized_MOS=False)

    return score_dict["SIG"]


def DNSMOS_OVRL(est_target, **kwargs):

    assert len(est_target.shape) == 1
    
    
    score_dict = compute_score(est_target, SAMPLING_RATE, is_personalized_MOS=False)

    return score_dict["OVRL"]

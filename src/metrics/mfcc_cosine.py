
import torch
import torchaudio
import torch.nn.functional as F
# from python_speech_feature import mfcc


def get_energy_mask(waveform, frame_length=400, hop_length=160, threshold=40.0):
    # Compute framewise RMS energy (dB)
    frames = waveform.unfold(1, frame_length, hop_length)
    rms = frames.pow(2).mean(dim=2).sqrt()
    energy_db = 20 * torch.log10(rms + 1e-8)

    # Threshold relative to max
    mask = energy_db > (energy_db.max() - threshold)

    
    return mask.squeeze(0)  # (num_frames,)


def mfcc_cosine_similarity(ref, deg, fs=8000, n_mfcc=20):


    ref = torch.tensor(ref, dtype=torch.float32)
    deg = torch.tensor(deg, dtype=torch.float32)

    if ref.ndim == 1:
        ref = ref.unsqueeze(0)  # (1, T)
    if deg.ndim == 1:
        deg = deg.unsqueeze(0)

    frame_length = 2048
    hop_length = 256
    mask = get_energy_mask(ref, frame_length, hop_length)


    mfcc_transform = torchaudio.transforms.MFCC(
        sample_rate=fs,
        n_mfcc=n_mfcc,
        melkwargs={"n_fft": frame_length, "hop_length": hop_length, "n_mels": 80}
    )

    ref_mfcc = mfcc_transform(ref.unsqueeze(0))   # (1, n_mfcc, time)
    deg_mfcc = mfcc_transform(deg.unsqueeze(0))

    T = min(ref_mfcc.shape[-1], deg_mfcc.shape[-1])
    ref_mfcc = ref_mfcc[..., :T].squeeze(0).T   # (time, n_mfcc)
    deg_mfcc = deg_mfcc[..., :T].squeeze(0).T

    ref_mfcc = ref_mfcc * mask
    deg_mfcc = deg_mfcc * mask

    # Cosine similarity per frame
    sims = F.cosine_similarity(ref_mfcc, deg_mfcc, dim=1)


    return sims.mean().item()

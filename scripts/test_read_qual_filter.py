from read_quality_filterer import *


def test_window_mean_scores():
    qstr = "IIIIII#####"
    meanquals = [40.0, 40.0, 32.4, 24.8, 17.2, 9.6, 2.0, ]
    nwindows = 0
    for i, meanq in window_mean_scores(qstr, winlen=5, phread=33):
        assert meanq == meanquals[i], "Wrong window score"
        nwindows = i
    assert nwindows == len(meanquals), "Too few windows"

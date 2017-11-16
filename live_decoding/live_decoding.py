# COMMAND: online2-wav-gmm-latgen-faster --config=./builds/pl-PL/0.0.1/exp/mono/conf/online_decoding.conf --word-symbol-table=./builds/pl-PL/0.0.1/exp/mono/graph/words.txt ./builds/pl-PL/0.0.1/exp/mono/graph/HCLG.fst "ark:echo SPEAKER UTTERANCE|" "scp:-" "ark:/dev/null"
from auto_audio_recorder import AutoAudioRecorder
from kaldi_decoder import KaldiDecoder

if __name__ == '__main__':
    decoder = KaldiDecoder('')
    decoder.initialize()

    with AutoAudioRecorder('FajQa', decoder) as recorder:
        recorder.start()
        input()
        recorder.stop()
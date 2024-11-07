import unittest
import pyaudio
import wave

class Test(unittest.TestCase):  
    def test_init(self):
        print("Hello from test.py")
        p = pyaudio.PyAudio()
        print(p.get_device_count())
        p.terminate()

    def test_soundplay(self):
        p = pyaudio.PyAudio()
        with wave.open('data/sound_source/hello_world.wav', 'rb') as wf:
            # パラメータの取得
            params = wf.getparams()

            # 出力ファイルの作成
            with wave.open('data/output/test.wav', 'wb') as output_wf:
                # 同じパラメータを設定
                output_wf.setparams(params)

                # WAVデータの読み込みと書き込み
                frames = wf.readframes(wf.getnframes())
                output_wf.writeframes(frames)

        # PyAudioオブジェクトの終了処理
        p.terminate()

 
if __name__ == '__main__':
    unittest.main()
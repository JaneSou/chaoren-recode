# -*- coding: utf-8-*-
"""
用于替换mic.class,以实现本地离线实时监听终端的I/O。适用于调试。与典型的麦克风不同
实现时, 叮当始终主动地侦听 local_mic。
"""

class Mic:
    prev = None

    def __init__(self, speaker, passive_sst_engine, active_stt_engine):
        self.stop_apssive = False
        self.skip_passive = False
        self.chatting_mode = False
        return

    def passiveListen(self, PERSONA):
        return  True, "CHAOREN"

    def activeListenToAllOptions(self, THRESHOLD = None, LISTEN = True, MUSIC = False):
        return [self.activeListen(THRESHOLD=THRESHOLD, LISTEN=LISTEN, MUSIC=MUSIC)]

    def activeListen(self, THRESHOLD=None, LISTEN=True, MUSIC=False):
        if not LISTEN:
            return self.prev

        input = raw_input("YOU: ")
        self.prev = input
        return input

    def say(self, phrase, OPTIONS=None, cache=False):
        print("CHAOREN: %s" % phrase)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Modulador_de_Amplitud
# Author: Jhonatan Franco_Jhonatan Valest_J1B_G4
# GNU Radio version: 3.10.5.1

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from CalculoPotenciaJ1B import CalculoPotenciaJ1B  # grc-generated hier_block
from Envolvente_Compleja_SSB_J1B_G4 import Envolvente_Compleja_SSB_J1B_G4  # grc-generated hier_block
from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
from gnuradio.fft import window
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import uhd
import time
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore



from gnuradio import qtgui

class Modulador_de_Amplitud(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Modulador_de_Amplitud", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Modulador_de_Amplitud")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "Modulador_de_Amplitud")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 12500000/32
        self.ka = ka = 1
        self.k = k = 1
        self.fm = fm = 1000
        self.fc = fc = 50e6
        self.GTX = GTX = 0
        self.B = B = 1
        self.Audio_rate = Audio_rate = 44100
        self.Am = Am = 1
        self.Ac = Ac = 125e-3

        ##################################################
        # Blocks
        ##################################################

        self._k_range = Range(0, 1, 1, 1, 200)
        self._k_win = RangeWidget(self._k_range, self.set_k, "habilita portadora", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._k_win)
        self._fc_range = Range(50e6, 2.2e9, 1e6, 50e6, 200)
        self._fc_win = RangeWidget(self._fc_range, self.set_fc, "frecuencia de portadora", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._fc_win)
        self._GTX_range = Range(0, 30, 1, 0, 200)
        self._GTX_win = RangeWidget(self._GTX_range, self.set_GTX, "Ganancia del transmisor", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._GTX_win)
        self._Ac_range = Range(0, 1, 1e-3, 125e-3, 200)
        self._Ac_win = RangeWidget(self._Ac_range, self.set_Ac, "Amplitud de la portadora (Ac)", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._Ac_win)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
            ",".join(("", '')),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,1)),
            ),
            "",
        )
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0.set_time_now(uhd.time_spec(time.time()), uhd.ALL_MBOARDS)

        self.uhd_usrp_sink_0.set_center_freq(fc, 0)
        self.uhd_usrp_sink_0.set_antenna("TX/RX", 0)
        self.uhd_usrp_sink_0.set_gain(GTX, 0)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=int(samp_rate),
                decimation=Audio_rate,
                taps=[],
                fractional_bw=0)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
            1024, #size
            samp_rate, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                if (i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self._ka_range = Range(0, 8, 0.01, 1, 200)
        self._ka_win = RangeWidget(self._ka_range, self.set_ka, "Coeficiente ka", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._ka_win)
        self._fm_range = Range(300, samp_rate/4, 100, 1000, 200)
        self._fm_win = RangeWidget(self._fm_range, self.set_fm, "frecuencia de mensaje", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._fm_win)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/home/labcom/Descargas/Audio_de_prueba.wav', True)
        self.Envolvente_Compleja_SSB_J1B_G4_0 = Envolvente_Compleja_SSB_J1B_G4(
            Ac=Ac,
            K=k,
        )
        self.CalculoPotenciaJ1B_0 = CalculoPotenciaJ1B(
            l_vect=1024,
        )

        self.top_layout.addWidget(self.CalculoPotenciaJ1B_0)
        self._B_range = Range(-1, 1, 2, 1, 200)
        self._B_win = RangeWidget(self._B_range, self.set_B, "cambio de banda", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._B_win)
        self._Am_range = Range(0, 8, 100e-3, 1, 200)
        self._Am_win = RangeWidget(self._Am_range, self.set_Am, "Amplitud del mensaje", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._Am_win)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.Envolvente_Compleja_SSB_J1B_G4_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.Envolvente_Compleja_SSB_J1B_G4_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.Envolvente_Compleja_SSB_J1B_G4_0, 0), (self.uhd_usrp_sink_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.CalculoPotenciaJ1B_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.Envolvente_Compleja_SSB_J1B_G4_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Modulador_de_Amplitud")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)

    def get_ka(self):
        return self.ka

    def set_ka(self, ka):
        self.ka = ka

    def get_k(self):
        return self.k

    def set_k(self, k):
        self.k = k
        self.Envolvente_Compleja_SSB_J1B_G4_0.set_K(self.k)

    def get_fm(self):
        return self.fm

    def set_fm(self, fm):
        self.fm = fm

    def get_fc(self):
        return self.fc

    def set_fc(self, fc):
        self.fc = fc
        self.uhd_usrp_sink_0.set_center_freq(self.fc, 0)

    def get_GTX(self):
        return self.GTX

    def set_GTX(self, GTX):
        self.GTX = GTX
        self.uhd_usrp_sink_0.set_gain(self.GTX, 0)

    def get_B(self):
        return self.B

    def set_B(self, B):
        self.B = B

    def get_Audio_rate(self):
        return self.Audio_rate

    def set_Audio_rate(self, Audio_rate):
        self.Audio_rate = Audio_rate

    def get_Am(self):
        return self.Am

    def set_Am(self, Am):
        self.Am = Am

    def get_Ac(self):
        return self.Ac

    def set_Ac(self, Ac):
        self.Ac = Ac
        self.Envolvente_Compleja_SSB_J1B_G4_0.set_Ac(self.Ac)




def main(top_block_cls=Modulador_de_Amplitud, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()

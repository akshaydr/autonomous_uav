#!/usr/bin/env python


# Kivy Example App for the slider widget
import rospy
from std_msgs.msg import Float64
from roscopter.msg import RC

import time

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.properties  import NumericProperty
from kivy.uix.button import Button

class WidgetContainer(GridLayout):
    def __init__(self, **kwargs):

        super(WidgetContainer, self).__init__(**kwargs)
        # 2 columns in grid layout
        self.roll_val = 1540
        self.pitch_val = 1517
        self.yaw_val = 1511
        self.throt_val = 1008
        self.channel = [1511, 1517, 1008, 1540, 1500, 2000, 1500, 1500]


        self.add_widget(Label(text='', halign='center'))
        self.add_widget(Label(text='Autonomous Quadcopter Controller', bold=True ,halign='center', font_size='25sp', italic=True))
        self.add_widget(Label(text='', halign='center'))

        self.cols = 3
        # self.set_cols(1, 1, 10)
        self.roll_control = Slider(min=1063, max =2016, size_hint_x=None, width = 550)
        self.roll_control.value_normalized = .5

        self.pitch_control = Slider(min=1017, max =2017, size_hint_x=None, width = 550)
        self.pitch_control.value_normalized = .5

        self.yaw_control = Slider(min=1011, max =2011, size_hint_x=None, width = 550)
        self.yaw_control.value_normalized = .5

        self.throttle_control = Slider(min=1008, max =2006, size_hint_x=None, width = 550)

        # 1st row - one label, one slider
        self.add_widget(Label(text='Roll', size_hint_x=None, width = 100))
        self.add_widget(self.roll_control)
        self.roll_control.bind(value=self.on_roll_value)
        # self.roll_control.value_normalized = .5
        self.rollValue = Label(text='1540', size_hint_x=None, width = 50)
        self.add_widget(self.rollValue)

        self.add_widget(Label(text='Pitch', size_hint_x=None, width = 100))
        self.add_widget(self.pitch_control)
        self.pitch_control.bind(value=self.on_pitch_value)
        self.pitchValue = Label(text='1517', size_hint_x=None, width = 50)
        self.add_widget(self.pitchValue)

        self.add_widget(Label(text='Yaw', size_hint_x=None, width = 100))
        self.add_widget(self.yaw_control)
        self.yaw_control.bind(value=self.on_yaw_value)
        self.yawValue = Label(text='1511', size_hint_x=None, width = 50)
        self.add_widget(self.yawValue)
        # self.roll_control.value_normalized = .5

        self.add_widget(Label(text='Throttle', size_hint_x=None, width = 100))
        self.add_widget(self.throttle_control)
        self.throttle_control.bind(value=self.on_throttle_value)
        self.throttleValue = Label(text='1008', size_hint_x=None, width = 50)
        self.add_widget(self.throttleValue)

        def arm_callback(instance):
            print('Arming')

        def init_callback(instance):
            print('Initialise')

        def disarm_callback(instance):
            print('DisArm')

        def reset_callback(instance):
            self.roll_control.value_normalized = .5
            self.pitch_control.value_normalized = .5
            self.yaw_control.value_normalized = .5
            # self.throttle_control.value_normalized = .0


        self.add_widget(Button(text='Arm', size_hint_x=None, width = 100, on_press=arm_callback))
        self.add_widget(Button(text='Initialise',size_hint_x=None, width = 550, on_press=init_callback))
        self.add_widget(Button(text='DisArm',size_hint_x=None, width = 100, on_press=disarm_callback))

        self.add_widget(Button(text='Reset',size_hint_x=None, width = 100, on_press=reset_callback))

    # def on_touch_up(self, touch):
    #     self.roll_control.value_normalized = .5
    #     self.pitch_control.value_normalized = .5
    #     self.yaw_control.value_normalized = .5


    def on_roll_value(self, instance, roll):
        self.rollValue.text = "%d"%roll
        self.roll_val = roll
        self.channel = [int(self.yaw_val), int(self.pitch_val), int(self.throt_val), int(self.roll_val), 1500, 2000, 1500, 1500]
        pub.publish(self.channel)


    def on_pitch_value(self, instance, pitch):
        self.pitchValue.text = "%d"%pitch
        self.pitch_val = pitch
        self.channel = [int(self.yaw_val), int(self.pitch_val), int(self.throt_val), int(self.roll_val), 1500, 2000, 1500, 1500]
        pub.publish(self.channel)


    def on_yaw_value(self, instance, yaw):
        self.yawValue.text = "%d"%yaw
        self.yaw_val = yaw
        self.channel = [int(self.yaw_val), int(self.pitch_val), int(self.throt_val), int(self.roll_val), 1500, 2000, 1500, 1500]
        pub.publish(self.channel)

    def on_throttle_value(self, instance, throttle):
        self.throttleValue.text = "%d"%throttle
        self.throt_val = throttle
        self.channel = [int(self.yaw_val), int(self.pitch_val), int(self.throt_val), int(self.roll_val), 1500, 2000, 1500, 1500]
        pub.publish(self.channel)
        # print "%d"%brightness


class controller(App):
    def build(self):
        widgetContainer = WidgetContainer()
        return widgetContainer

# Run the app

if __name__ == '__main__':
    rospy.init_node('controller')
    pub = rospy.Publisher('control_val', RC, queue_size=10)
    controller().run()

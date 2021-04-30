import gradio as gr
from utils.module import ModelManager
from utils.loader import DatasetManager
from utils.process import Processor


class Main:

  def __init__(self):
    self.running = True

  def handle_query(self, query):
    """ read in wuqery get intetns/slots then pull data"""
    intents, slots = self.get_intent_and_slots(query)
    return "this is the answer you/re looking for"


  def get_required_data(self, intent, slots):
    """this will get the right data from the spreadsheet"""
    data = None
    return data

  def get_intent_and_slots(self, text):
    """will return the intents and slots"""
    intent = None
    slots = []
    return intent, slots

  def demo(self, name):
    return "Hello " + name + "!"


if __name__ == "__main__":

  demo = Main()
  iface = gr.Interface(
    fn=demo.demo,
    inputs=gr.inputs.Textbox(lines=2, placeholder="Name Here..."),
    outputs="text")
  iface.launch()
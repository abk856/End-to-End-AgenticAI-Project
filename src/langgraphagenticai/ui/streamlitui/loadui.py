import streamlit as st
import os
from datetime import date

from lanchain_core.messages import AIMessage, HumanMessage


class LoadStreamlitUI:
    def __init__(self):
        
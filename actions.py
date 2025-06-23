# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionChooseBook(Action):
    def name(self) -> Text:
        return "action_choose_book"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        book = tracker.latest_message.get('text', '').lower()

        if "cooking" in book:
            dispatcher.utter_message(response="utter_cooking_book")
        elif "legends" in book:
            dispatcher.utter_message(response="utter_legends_book")
        elif "royal" in book:
            dispatcher.utter_message(response="utter_royal_book")
            return [SlotSet("knows_order", True)]
        else:
            dispatcher.utter_message(text="I couldn't find that book.")
        return []

class ActionEnterCode(Action):
    def name(self) -> Text:
        return "action_enter_code"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        text = tracker.latest_message.get('text', '')
        if "492" in text or "4 9 2" in text:
            dispatcher.utter_message(response="utter_code_success")
            return []
        elif "4" in text and "9" in text and "2" in text:
            dispatcher.utter_message(response="utter_code_wrong_order")
        else:
            dispatcher.utter_message(response="utter_code_wrong")
        return []

class ActionRecallMemory(Action):
    def name(self) -> Text:
        return "action_recall_memory"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        mem_text = []
        if tracker.get_slot("mem_east"):
            mem_text.append("King Alric - 4")
        if tracker.get_slot("mem_north"):
            mem_text.append("Queen Berena - 9")
        if tracker.get_slot("mem_west"):
            mem_text.append("Prince Cedric - 2")

        if mem_text:
            dispatcher.utter_message(response="utter_memory_recall")
            for line in mem_text:
                dispatcher.utter_message(text=line)
        else:
            dispatcher.utter_message(response="utter_memory_empty")
        return []

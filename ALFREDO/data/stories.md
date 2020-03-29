
## story_0
* greet
	- utter_greet
* inform
	- utter_ask_location
* inform{"location": "India"}
	- slot{"location": "India"}
	- actions.Inform_Action
	- slot{"location": "India"}
* goodbye
	- utter_goodbye

## story_1
* greet
	- utter_greet


## story_2
* goodbye
	- utter_goodbye

## story_3
* inform
	- actions.Inform_Action
## Generated Story 9065889736530049489
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform

## Generated Story -5318267946307836256
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform
    - actions.Inform_Action
    - actions.Inform_Action
    - actions.Inform_Action
* goodbye
    - utter_goodbye

## Generated Story -8257919706177990961
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform
    - action_default_fallback
    - rewind
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "world"}
    - slot{"location": "world"}
    - actions.Inform_Action
* inform{"location": "usa"}
    - slot{"location": "usa"}
    - actions.Inform_Action
* greet
    - utter_greet
* inform{"location": "France"}
    - slot{"location": "France"}
    - actions.Inform_Action
* greet
    - action_default_fallback
    - rewind
* greet
    - utter_greet
* inform


#!/usr/bin/python3
""" Test delete feature
"""
from models.engine.file_storage import FileStorage
from models.state import State
from models.place import Place
fs = FileStorage()

all_states = fs.all()
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
        print(all_states[state_key])

# Create a new State
new = Place()
new.name = "Cal"
fs.new(new)
fs.save()
print("New State: {}".format(new))

# All States
all_state = fs.all(Place)
print("All States: {}".format(len(all_state.keys())))
for state_key in all_state.keys():
    print(all_state[state_key])


# All States
# Create a new State
new_state = State()
new_state.name = "California"
fs.new(new_state)
fs.save()
print("New State: {}".format(new_state))

all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
        print(all_states[state_key])

fs.delete(new_state)

# All States
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

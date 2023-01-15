A simple ML library.

To install the package is to just run the command: pip install open_py_ml

One example of it is:

<br>
<code>
import open_py_ml
# In this case we are making a very simple chatbot
data = {
    "Hi!": "Hello there.",
    "Why were you made?": "I was made to be an example of machine learning AI's using open_py_ml library"
} # This data is actually usually loaded from a .json file.

model = open_py_ml.Brain(data, 0.5) # Create a new brain with threshold 50%, With the data we provided

print(model.forward("hi!")) # Prints Hello there.
print(model.forward("Why were you made")) # Prints I was made to be an example...
</code>
<br>

Another example (if you have data.json):

<br>
<code>
import open_py_ml
# In this case we are making a very simple chatbot

model = open_py_ml.load("data.json", 0.5) # Create a new brain with threshold 50%, With the data we provided

\# Use print(model.forward([whatever is in the json file])), To print some data that is from the json file
</code>
<br>

<br>
<code>
class Brain:<br>
    """<br>
    A brain. An Artificial intelligence (AI)'s data and runner.<br>
    Data: First argument in __init__(), Data is for the training data key/values<br>
    Threshold: Second argument in __init(), Threshold is for the percentage of which the AI finds<br>
    That the data is simular enough to the input string of which it is accepted<br>
    NOTE: This only works with strings now.<br>
    """<br>
    <br>
    def __init__(self, data: dict or None, threshold: float):<br>
        """<br>
        Initializes a new brain.<br>
        """<br>
    <br>
    def forward(self, data: str) -> str:<br>
        """<br>
        Gives a string for the Artificial intelligence (AI) to process.<br>
        """<br>
</code>
</code>
</code>


As you can see, This is just the way the brain is organized.<br>
You can only just use this, and you would have A good time.<br>
But for quickly loading the brain. By quickly<br> I mean without having to load the file yourself with "open()"
<br> You can actually just use load(filename, threshold), and save(ai, threshold).<br>
Note that load and save just save with json.<br>
This can only handle strings.

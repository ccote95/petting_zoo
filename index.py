from slithering.cobra import Cobra
from slithering.python import Python
from swimming.crocodile import Crocodile
from swimming.dolphin import Dolphin
from swimming.frog import Frog
from swimming.otter import Otter
from swimming.penguin import Penguin
from swimming.shark import Shark
from swimming.turtle import Turtle
from swimming.whale import Whale
from walking.eagle import Eagle
from walking.gecko import Gecko
from walking.kangaroo import Kangaroo
from walking.llama import Llama  # Import the class Llama, not the module


miss_fuzz = Llama("Miss Fuzz", "domestic llama", "morning", "Llama Chow" )

bob = Gecko("bob", "gecko", "midday", "Gecko Chow")
print(bob)

miss_fuzz.feed()
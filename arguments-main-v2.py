# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

def greet(name, greeting_template = "Hello, <name>!"):
    return(greeting_template.replace("<name>", name))

# print(greet("Doc"))
# print(greet('Bob', "What's up, <name>!"))


# PLEASE READ
# the url https://www.smartconversion.com/otherInfo/gravity_of_planets_and_the_sun.aspx is not working, I am guessing I was getting a list of different forces per planet
# including an external link is very irritating by the way. imagine when it does not work

gravitational_forces = {
    "sun" : 274,
    "jupiter": 24.9,
    "neptune": 11.1,
    "saturn": 10.4,
    "earth": 9.8,
    "uranus": 8.9,
    "venus": 8.9,
    "mars": 3.7,
    "mercury": 3.7,
    "moon": 1.6,
    "pluto" : 8.6
}

def force(mass, body="earth"):
    gravitational_force_of_body = gravitational_forces[body]
    force_of_body = mass * gravitational_force_of_body
    return force_of_body


# I am not sure I could follow this bit of the explanattion, though it seems to pertan to astronomy more than python

G = 9.8
def pull(mass1, mass2, distance):
    return G*(mass1*mass2)/(distance**2)

print(pull(800, 1500, 3))


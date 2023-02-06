import random

R_TALKING = "I don't like talking much  because I'm am bit introvert!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"


def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "You can refer Sakura or Avimanyu",
                "What does that mean?"][
        random.randrange(4)]
    return response
# Викторов Александр Андеевич 11.5.2

from game import Game

if __name__ == "__main__":
    try:
        game = Game()
        game.start()
    except Exception:
        print("Во время работы программы произошла ошибка! - {}"
              .format(Exception))

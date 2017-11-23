from income_structure import Diagrams

if __name__ == "__main__":
    filename = "data_2017-12-27.csv"
    diagram = Diagrams()
    diagram.load(filename)
    diagram.prnt_diagram()

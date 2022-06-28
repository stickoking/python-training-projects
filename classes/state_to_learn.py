import pandas


class StateToLearn:

    def __init__(self, screen, data):
        self.new_data = data.state.to_list()
        self.screen = screen
        self.to_learn = pandas.DataFrame(self.new_data);

    def print_csv(self, data):
        for x in data:
            self.new_data.remove(x.title())

        self.to_learn = pandas.DataFrame(self.new_data)
        self.to_learn.to_csv("to_learn.csv")
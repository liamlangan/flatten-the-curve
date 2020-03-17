import matplotlib.pyplot as plt
import matplotlib.style
from conf import *
import numpy as np

matplotlib.style.use('ggplot')


class Plot:
    def __init__(self, agents):
        self.agents = agents
        plt.ion()
        self.fig, self.ax = plt.subplots(1, figsize=(16, 2))
        self.times = [0]
        self.values = np.array([self.get_infection_counts()])

    def update(self, t):
        self.times.append(t)

        infection_counts = self.get_infection_counts()

        self.values = np.append(self.values, [infection_counts], axis=0)

        if t % plot_interval == 1:
            self.ax.clear()

            self.ax.grid(True)
            self.ax.set_xlim(0, max_t)
            self.ax.set_ylim(0, agent_num)

            self.ax.fill_between(self.times, 0, self.values[:, 1] +self.values[:, 0] +self.values[:, 2] +self.values[:, 0],
                                 color=np.array(agent_colors[3]) / 255)
            self.ax.fill_between(self.times, 0, self.values[:, 1] +self.values[:, 0] +self.values[:, 2],
                                 color=np.array(agent_colors[2]) / 255)
            self.ax.fill_between(self.times, 0, self.values[:, 1] +self.values[:, 0], color=np.array(agent_colors[0]) / 255)
            self.ax.fill_between(self.times, 0, self.values[:, 1], color=np.array(agent_colors[1]) / 255)

            self.fig.tight_layout()
            self.fig.canvas.draw()
            self.fig.show()
            self.fig.savefig("plots/plot_{:05d}.png".format(t))

    def get_infection_counts(self):
        infection_counts = [0, 0, 0, 0]
        for agent in self.agents:
            infection_counts[agent.infection] += 1
        return infection_counts
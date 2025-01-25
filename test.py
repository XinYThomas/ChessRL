#
from kaggle_environments import make

#
env = make("chess", debug=True)
#
# # this should run a game in the environment between two random bots
# # NOTE: each game starts from a randomly selected opening

env.render(mode="html")





# print(result)
# import gym
# env = gym.make('CartPole-v1', render_mode='human')
# env.reset()
#
# for _ in range(50):
#     env.render()
#
#     action = env.action_space.sample()
#     env.step(action)
#
# env.close()

# from kaggle_environments import make
#
# # Setup a tictactoe environment.
# env = make("tictactoe")
#
# # Basic agent which marks the first available cell.
# def my_agent(obs):
#   return [c for c in range(len(obs.board)) if obs.board[c] == 0][0]
#
# # Run the basic agent against a default agent which chooses a "random" move.
# env.run([None, "random"])
# env.render(mode="human")
# # Render an html ipython replay of the tictactoe game.
# help( env.render(mode="human"))
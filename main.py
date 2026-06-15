from game import ResourceGame

print("\n")
print("########################################")
print("# COMPETITIVE RESOURCE ALLOCATION GAME #")
print("########################################")

print("\nAgents Entering Arena...")
print("Alpha  -> Aggressive Strategy")
print("Beta   -> Balanced Strategy")
print("Gamma  -> Conservative Strategy")

game = ResourceGame()

game.play()

game.declare_winner()
from agent import Agent
import time

class ResourceGame:

    def __init__(self):

        self.resources = 50

        self.agents = [
            Agent("Alpha", "Aggressive"),
            Agent("Beta", "Balanced"),
            Agent("Gamma", "Conservative")
        ]

    def show_scores(self):

        print("\nCURRENT SCOREBOARD")
        print("-" * 35)

        for agent in self.agents:
            print(
                f"{agent.name:10} | "
                f"{agent.strategy:12} | "
                f"Score = {agent.score}"
            )

        print("-" * 35)

    def play(self):

        round_no = 1

        while self.resources > 0:

            print("\n")
            print("=" * 50)
            print(f"ROUND {round_no}")
            print("=" * 50)

            for agent in self.agents:

                if self.resources <= 0:
                    break

                take = agent.choose_resources(
                    self.resources
                )

                self.resources -= take
                agent.score += take

                print(
                    f"{agent.name} "
                    f"({agent.strategy}) "
                    f"captured {take} resources"
                )

                time.sleep(0.5)

            print(
                f"\nResources Left : {self.resources}"
            )

            self.show_scores()

            round_no += 1

        print("\n")
        print("=" * 50)
        print("GAME OVER")
        print("=" * 50)

    def declare_winner(self):

        winner = max(
            self.agents,
            key=lambda a: a.score
        )

        print("\nFINAL RESULTS")
        print("-" * 35)

        for agent in self.agents:
            print(
                f"{agent.name} : {agent.score}"
            )

        print("\n🏆 WINNER :", winner.name)
        print("Strategy :", winner.strategy)
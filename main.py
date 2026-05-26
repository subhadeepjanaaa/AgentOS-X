from core.brain import Brain
from core.router import Router
from core.memory import MemorySystem
from agents.ceo_agent import CEOAgent

brain = Brain()
router = Router()
memory = MemorySystem()
ceo = CEOAgent()

task = input("Enter Task: ")

decision = brain.think(task)

department = router.route_task(decision)

ceo.execute_strategy(department)

memory.save_memory(task, decision)

memory.show_history()
from core.brain import Brain
from core.router import Router
from core.memory import MemorySystem
from core.communicator import Communicator
from core.database import DatabaseManager

from agents.ceo_agent import CEOAgent
from agents.worker_agent import WorkerAgent

brain = Brain()
router = Router()
memory = MemorySystem()
communicator = Communicator()
database = DatabaseManager()

ceo = CEOAgent()
worker = WorkerAgent()

task = input("Enter Task: ")

# Brain Decision
decision = brain.think(task)

# Route Task
department = router.route_task(decision)

# CEO Strategy
ceo.execute_strategy(department)

# Communication
communicator.send_message(department, task)

# Worker Execution
result = worker.execute_task(task)

# Save Local Memory
memory.save_memory(task, decision)

# Save Database Task
database.save_task(task, decision, department)

# Save Database Memory
database.save_memory(
    "Worker Agent",
    result
)

# Save System Log
database.save_log(
    "AgentOS-X",
    "Enterprise workflow executed successfully"
)

# Show Local Memory
memory.show_history()

print(f"\n[Final Enterprise Output] {result}")
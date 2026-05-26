class MemorySystem:

    def __init__(self):

        self.history = []

    def save_memory(self, task, decision):

        memory_entry = {
            "task": task,
            "decision": decision
        }

        self.history.append(memory_entry)

        print("\n[Memory System] Task Saved")

    def show_history(self):

        print("\n====== MEMORY HISTORY ======")

        for item in self.history:

            print(f"Task: {item['task']}")
            print(f"Decision: {item['decision']}")
            print("---------------------------")
class WorkerAgent:

    def execute_task(self, task):

        print("\n[Worker Agent] Starting Task Execution...")

        if "report" in task.lower():

            result = "Enterprise report generated successfully"

        elif "analysis" in task.lower():

            result = "Enterprise analytics completed successfully"

        else:

            result = "Task processed successfully"

        print(f"[Worker Result] {result}")

        return result
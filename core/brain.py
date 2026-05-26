class Brain:

    def think(self, task):

        print(f"\n[Brain] Received Task: {task}")

        if "report" in task.lower():
            decision = "Send task to Worker Agent"

        elif "analysis" in task.lower():
            decision = "Send task to Analytics Agent"

        else:
            decision = "Send task to CEO Agent"

        print(f"[Brain Decision] {decision}")

        return decision
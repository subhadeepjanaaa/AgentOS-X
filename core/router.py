class Router:

    def route_task(self, decision):

        print("\n[Router] Routing Task...")

        if "Worker Agent" in decision:

            department = "Worker Department"

        elif "Analytics Agent" in decision:

            department = "Analytics Department"

        else:

            department = "CEO Department"

        print(f"[Router] Task sent to: {department}")

        return department
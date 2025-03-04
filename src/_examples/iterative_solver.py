import logging

from mojentic.agents.iterative_problem_solver import IterativeProblemSolver

logging.basicConfig(level=logging.WARN)

from mojentic.llm.tools.date_resolver import ResolveDateTool
from mojentic.llm.tools.ask_user_tool import AskUserTool
from mojentic.llm import LLMBroker


def main():
    # llm = LLMBroker(model="MFDoom/deepseek-r1-tool-calling:14b")
    llm = LLMBroker(model="qwen2.5:14b")
    # llm = LLMBroker(model="llama3.3-70b-32k")

    user_request = """
    We want to run a small conference event with 40-60 participants. We need to find a suitable venue, organize and open up
    registration.
    """.strip()

    # user_request = "What's the date next Friday?"

    ooda = IterativeProblemSolver(
        llm=llm,
        user_request=user_request,
        available_tools=[AskUserTool(), ResolveDateTool()],
        max_loops=5
    )
    result = ooda.run()
    print(user_request)
    print(result)


if __name__ == "__main__":
    main()

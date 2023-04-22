"""
agentを利用した高度な対話エージェント
"""
from langchain.agents import AgentExecutor, initialize_agent
from langchain.memory import ConversationBufferMemory

from controls.llm import chatGpt

memory = ConversationBufferMemory(memory_key="chat_history")

agent_chain: AgentExecutor = initialize_agent(
    tools=[],
    llm=chatGpt,
    agent="conversational-react-description",
    verbose=True,
    memory=memory,
)

user_input = input("You: ")

while True:
    res = agent_chain.run(input=user_input)
    print(f"AI: {res}")
    user_input = input("You: ")
    if user_input == "exit":
        break

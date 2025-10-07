
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.agents import load_tools
from langchain_community.chat_models import ChatOllama

from lib.utils import Constants

__constants = Constants.get_instance()
model=__constants.local_model
llm = ChatOllama(model=model)
tools = load_tools(["llm-math"], llm=llm)

agent = initialize_agent(tools,
                         llm,
                         agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                         verbose=True)

agent.run("If my age is half of my dad's age and he is going to be 60 next year, what is my current age?")

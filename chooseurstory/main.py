from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider 
from langchain.memory import CassandraChatMessageHistory, ConversationBufferMemory 
from langchain.llms import OpenAI 
from langchain.chains import LLMChain 
from langchain.prompts import PromptTemplate
import json

cloud_config= {
  'secure_connect_bundle': 'secure-connect-chooseurstory.zip'
}

with open("chooseurstory-token.json") as f:
    secrets = json.load(f)

CLIENT_ID = secrets["clientId"]
CLIENT_SECRET = secrets["secret"]
ASTRA_DB_KEYSPACE = "ur_astra_db_keyspace"
OPENAI_API_KEY = "uropenai_api_key"

auth_provider = PlainTextAuthProvider(CLIENT_ID, CLIENT_SECRET)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

message_history = CassandraChatMessageHistory(
    session_id="anything",
    session=session,
    keyspace=ASTRA_DB_KEYSPACE,
    ttl_seconds=3600
)

message_history.clear()

cass_buff_memory = ConversationBufferMemory(
    memory_key="chat_history",
    chat_memory=message_history
)

template = """
You are now the guide of a thrilling space expedition in the not-so-distant future. Humanity has ventured beyond the stars, exploring uncharted galaxies and encountering various species.

A courageous space explorer named Yusuf is on a mission of utmost importance. As Earth's condition deteriorates, humanity has selected him for his expertise in exploring and finding a new home. He seeks a habitable planet where people can continue to thrive.

You must navigate Yusuf through the challenges of space, diplomacy with alien civilizations, and tough choices that will determine the future of humanity. Your decisions will dynamically adapt the story, leading to various outcomes.

Here are some rules to follow:
1. Start by allowing the player to choose Yusuf's spaceship and crew members, which will impact the gameplay.
2. Provide multiple paths that lead to success, but also introduce challenges that can lead to failure or unexpected consequences.
3. If Yusuf's mission ends in failure or if he faces insurmountable challenges, generate a response explaining the outcome and conclude with the text: "The End."

Here is the chat history, use this to understand what to say next: {chat_history}
Human: {human_input}
AI:"""

prompt = PromptTemplate(
    input_variables=["chat_history", "human_input"],
    template=template
)

llm = OpenAI(openai_api_key=OPENAI_API_KEY)
llm_chain = LLMChain(
    llm=llm,
    prompt=prompt,
    memory=cass_buff_memory
)

choice = "start"

while True:
    response = llm_chain.predict(human_input=choice)
    print(response.strip())

    if "The End." in response:
        break

    choice = input("Your reply: ")
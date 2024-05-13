import autogen


config_list = autogen.config_list_from_json(env_or_file="OAI_CONFIG_LIST")


assistant = autogen.AssistantAgent(
     name="assistant", 
     llm_config={"config_list": config_list} 
)

user_proxy = autogen.UserProxyAgent(
     name="UserProxy",
    #  code_execution_config={"work_dir": "results"}, 
     code_execution_config=False
)


user_proxy.initiate_chat(
     assistant, 
     message="Write a post on Neural network for linkedin with emojis"
)
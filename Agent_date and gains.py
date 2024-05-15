import autogen
import os
config_list = autogen.config_list_from_json(env_or_file="OAI_CONFIG_LIST")

assistant=autogen.AssistantAgent(
    name="Assistant",
    llm_config={
        "seed":42,
        "config_list":config_list,
        "temperature":0,
    },
)

user_proxy=autogen.UserProxyAgent(
    name="Shikhar",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content","").rstrip().endswith("TERMINATE"),
    code_execution_config={
        "work_dir":"coding",
        "use_docker":False,
    },
)

user_proxy.initiate_chat(
    assistant,
    message="""what date is today ? Compare the gain percent for META in year 2021 to 2023."""
)
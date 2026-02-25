from mal.adapter.openai import Model


deepseek = Model("deepseek/deepseek-chat", name="DeepSeek-V3")
deepseek_reasoner = Model("deepseek/deepseek-reasoner", name="DeepSeek-R1")

qwen = Model("qwen/qwen3.5-plus", name="Qwen 3.5")

kimi_k2 = Model("moonshot/kimi-k2-0905-preview", name="Kimi K2")
kimi_reasoner = Model("moonshot/kimi-2.5", name="Kimi K2.5")

gpt = Model("openai", name="GPT-5.2")

local = Model("local/qwen3.5-nt", name="Qwen3.5-35B-A3B")
local_reasoner = Model("local/qwen3.5", name="Qwen3.5-35B-A3B Thinking")

default = qwen

from mal.adapter.openai import Model


deepseek = Model("deepseek/deepseek-chat", name="DeepSeek-V3")
deepseek_reasoner = Model("deepseek/deepseek-reasoner", name="DeepSeek-R1")

qwen = Model("qwen")

kimi_k2 = Model("moonshot/kimi-k2-0905-preview", name="Kimi K2")
kimi_reasoner = Model("moonshot/kimi-2.5", name="Kimi K2.5")

gpt = Model("openai")

local = Model("local/qwen3.5-nt", name="Qwen3.5-35B-A3B")
local_reasoner = Model("local/qwen3.5", name="Qwen3.5-35B-A3B Thinking")

omlx = Model("omlx", name="Gemma-4-26B")

default = qwen

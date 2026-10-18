from mal.adapter.openai import Model


deepseek = Model("deepseek")

qwen = Model("qwen")

kimi = Model("moonshot")

gpt = Model("openai")

local = Model("local/qwen3.6-35b", name="Qwen3.6-35B-A3B")
local_reasoner = Model("local/qwen3.6-35b-thinking", name="Qwen3.6-35B-A3B Thinking")

omlx = Model("omlx", name="Qwen3.6-35B-A3B MLX")

default = deepseek

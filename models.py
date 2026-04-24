from mal.adapter.openai import Model


deepseek_flash = Model("deepseek/deepseek-v4-flash", name="DeepSeek-V4-Flash")
deepseek_pro = Model("deepseek/deepseek-v4-pro", name="DeepSeek-V4-Pro")

qwen = Model("qwen/qwen3.5-plus")

kimi_k2 = Model("moonshot/kimi-k2-0905-preview", name="Kimi K2")
kimi_reasoner = Model("moonshot/kimi-2.6", name="Kimi K2.6")

gpt = Model("openai")

local = Model("local/qwen3.6-nt", name="Qwen3.6-35B-A3B")
local_reasoner = Model("local/qwen3.6", name="Qwen3.6-35B-A3B Thinking")

omlx = Model("omlx", name="Qwen3.6-35B-A3B MLX")

default = deepseek_flash

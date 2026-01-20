from mal.adapter.openai import Model


deepseek = Model("deepseek/deepseek-chat", name="DeepSeek-V3")
deepseek_reasoner = Model("deepseek/deepseek-reasoner", name="DeepSeek-R1")

qwen = Model("qwen/qwen-plus-latest", name="Qwen Plus")
qwen_max = Model("qwen/qwen3-max-preview", name="Qwen Max")
qwen_coder = Model("qwen/qwen3-coder-plus", name="Qwen-Coder Plus")

kimi_k2 = Model("moonshot/kimi-k2-0905-preview", name="Kimi K2")
kimi_reasoner = Model("moonshot/kimi-thinking-preview", name="Kimi Thinking")

openrouter_gemini_flash = Model("openrouter/google/gemini-3-flash-preview", name="Gemini 3 Flash")
openrouter_gemini_pro = Model("openrouter/google/gemini-3-pro-preview", name="Gemini 3 Pro")

local = Model("local/qwen3", name="Qwen3-30B-A3B 2507")
local_reasoner = Model("local/qwen3-thinking", name="Qwen3-30B-A3B 2507 (Thinking)")

default = qwen

from mal.adapter.openai import Model


deepseek = Model("deepseek/deepseek-chat", name="DeepSeek-V3")
deepseek_reasoner = Model("deepseek/deepseek-reasoner", name="DeepSeek-R1")

qwen = Model("qwen/qwen-plus-latest", name="Qwen Plus")
qwen_max = Model("qwen/qwen3-max-preview", name="Qwen Max")
qwen_coder = Model("qwen/qwen3-coder-plus", name="Qwen-Coder Plus")

kimi_k2 = Model("moonshot/kimi-k2-0905-preview", name="Kimi K2")
kimi_reasoner = Model("moonshot/kimi-thinking-preview", name="Kimi Thinking")

openrouter_gemini_flash = Model("openrouter/google/gemini-2.5-flash", name="Gemini 2.5 Flash")
openrouter_gemini_pro = Model("openrouter/google/gemini-2.5-pro", name="Gemini 2.5 Pro")
openrouter_grok = Model("openrouter/x-ai/grok-4", name="Grok 4")
openrouter_k2 = Model("openrouter/moonshotai/kimi-k2", name="Kimi K2")

local = Model("local/qwen3", name="Qwen3-30B-A3B 2507")
local_reasoner = Model("local/qwen3-thinking", name="Qwen3-30B-A3B 2507 (Thinking)")
local_coder = Model("local/qwen3-coder", name="Qwen3-Coder-Flash")

default = deepseek

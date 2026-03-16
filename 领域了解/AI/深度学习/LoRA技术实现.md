* LoRA: Low-Rank Adaptation，低秩自适应
* 原理： 冻结原始模型参数， 通过训练低秩矩阵训练， 随后合并到原始参数。实现`微调`
* 实现
```
pip install peft transformers datasets
```

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import LoraConfig, get_peft_model

# 1. 加载基础模型（例如GPT-2，也可以是LLaMA、DeepSeek等）
model_name = "gpt2"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# 2. 配置LoRA参数（关键！）
lora_config = LoraConfig(
    r=8,                 # 秩的大小 —— 这正是我们之前讨论的“r”
    lora_alpha=32,       # 缩放因子，类似学习率缩放
    target_modules=["q_proj", "v_proj"],  # 要注入LoRA的模块（常见于注意力层）
    lora_dropout=0.1,    # Dropout比例
    bias="none",         # 是否训练偏置
    task_type="CAUSAL_LM" # 任务类型
)

# 3. 将LoRA应用到模型上
lora_model = get_peft_model(model, lora_config)

# 4. 查看可训练参数数量
lora_model.print_trainable_parameters()
# 输出示例：trainable params: 294,912 || all params: 124,734,720 || trainable%: 0.2364

# 保存LoRA权重（仅几MB）
lora_model.save_pretrained("./my-lora-adapter")
# 加载时
from peft import PeftModel
loaded_model = PeftModel.from_pretrained(base_model, "./my-lora-adapter")

```

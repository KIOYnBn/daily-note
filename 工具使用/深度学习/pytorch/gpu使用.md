* 判断是否存在gpu： nvidia-smi
* 判断可用gpu数量
```python
{
torch.cuda.device_count()
}
```
---
* 将张量或网络存储在gpu
```python
{
x = torch.ones(2, 3,device=try_gpu())
x.device

net = nn.Sequential(nn.Linear(3, 1))
net = net.to(device=try_gpu())
net[0].weight.data.device
```

# 多gpu共同运行
## FSDP法


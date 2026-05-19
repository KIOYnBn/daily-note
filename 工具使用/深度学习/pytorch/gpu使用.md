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

# 分布式
## device确定
```python
import torch, os
from dataclasses import dataclass

@dataclass
class InfoCuda:
	success: bool
	local_rank: int
	device: torch.device

def setup_distributed() -> InfoCuda:
	"""Setup distributed training if available"""
	if torch.cuda.is_available() and torch.cuda.device_count() >1:
		try:
			torch.distributed.init_process_group(backend="nccl")
			local_rank = int(os.environ.get("LOCAL_RANK", 0))
			torch.cuda.set_device(local_rank)
			device = torch.device("cuda", local_rank)
			return InfoCuda(True, local_rank, device)
		except Exception as e:
			print(f"Failed to initialize distributed training:{e} and would use cpu device")
			return InfoCuda(False, 0, torch.device("cuda"))
	else:return InfoCuda(False, 0, torch.device("cuda" if torch.cuda.is_available() else "cpu"))
		
```
---
## 数据分发
```python
    # Create samplers
def creat_dataloader():
    if is_distributed:

        train_sampler = torch.utils.data.distributed.DistributedSampler(train_list)

        valid_sampler = torch.utils.data.distributed.DistributedSampler(valid_list)

    else:

        train_sampler = sampler.SubsetRandomSampler(train_list)

        valid_sampler = sampler.SubsetRandomSampler(valid_list)
        
		# Create data loaders

    if is_distributed:

        train_loader = torch.utils.data.DataLoader(

            train_list, batch_size=batch_size, sampler=train_sampler,

            num_workers=0, collate_fn=stack_fn_train, drop_last=False

        )

        valid_loader = torch.utils.data.DataLoader(

            valid_list, batch_size=batch_size, sampler=valid_sampler,

            num_workers=0, collate_fn=stack_fn_valid, drop_last=False

        )

    else:

        train_loader = torch.utils.data.DataLoader(

            train_dataset, batch_size=batch_size, sampler=train_sampler,

            num_workers=0, collate_fn=stack_fn_test, drop_last=False

        )

        valid_loader = torch.utils.data.DataLoader(

            valid_dataset, batch_size=batch_size, sampler=valid_sampler,

            num_workers=0, collate_fn=stack_fn_test, drop_last=False

        )
```
---
## Model
```python
from torch.nn.parallel import DistributedDataParallel as DDP
if is_distributed:

	model = DDP(model, device_ids=[local_rank], output_device=local_rank, find_unused_parameters=True)
```

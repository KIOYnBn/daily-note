```python
class Encoder(nn.Module):
	"""Convolutional encode for protein feature extraction"""
	def __init__(
		self, protein_dim:int, hid_dim:int, n_layers:int,
		kernel_size:int, dropout:float, device:torch.device):
		super().__init__()
		# 便于通过padding保持序列不变
		assert kernel_size%2==1, "Kernel size must be odd"
		self.input_dim = protein_dim
		self.hid_dim = hid_dim
		self.kernel_size=kernel_size
		self.n_layers = n_layers
		self.device = device
		self.scale = torch.sqrt(torch.FloatTensor([0.5])).to(device)
		self.convs = nn.ModuleList([
		nn.Conv1d(hid_dim, 2*hid_dim, kernel_size, padding=(kernel_size-1) // 2)
			for _ in range(n_layers)
		])
		self.dropout = nn.Dropout(dropout)
		self.fc = nn.Linear(protein_dim, hid_dim)
		self.ln = nn.LayerNorm(hid_dim)
		
	def forward(self, protein:torch.Tensor)->torch.Tensor:
		"""
		Forward pass of encoder.
		Args:
			protein: Portein embeddings [ batch_size, seq_len, protein_dim]
		Returns:
			Encoded features [batch_size, seq_len, hid_dim]
		"""
		conv_input = self.fc(protein).permute(0, 2, 1)
		for conv in convs:
			conved = conv(self.dropout(conv_input))
			conved = F.glu(conved, dim=-1)
			conved = (conved+conv_input)*self.scale
			conv_input = conved
		conved = self.ln(conved.permute(0, 2, 1))
		return conved
```

	
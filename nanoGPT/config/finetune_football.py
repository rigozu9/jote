import time

out_dir = 'out-football'
eval_interval = 5
eval_iters = 40
wandb_log = False # feel free to turn on
wandb_project = 'football'
wandb_run_name = 'ft-' + str(time.time())

dataset = 'football'
init_from = 'gpt2'

# only save checkpoints if the validation loss improves
always_save_checkpoint = False

# the number of examples per iter:
# 1 batch_size * 32 grad_accum * 1024 tokens = 32,768 tokens/iter
# shakespeare has 301,966 tokens, so 1 epoch ~= 9.2 iters
batch_size = 1
gradient_accumulation_steps = 32
max_iters = 20

# finetune at constant LR
learning_rate = 3e-5
decay_lr = False
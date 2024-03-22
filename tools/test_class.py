import torch

from mmaction.apis import init_recognizer, inference_recognizer

config_file = 'configs/recognition/slowfast/slowfast_r152_r50_video_4x16x1_256e_construction_rgb.py'
# download the checkpoint from model zoo and put it in `checkpoints/`
checkpoint_file = 'work_dirs/slowfast_r152_r50_video_4x16x1_256e_construction_rgb/latest.pth'

# assign the desired device.
device = 'cuda:0' # or 'cpu'
device = torch.device(device)

 # build the model from a config file and a checkpoint file
model = init_recognizer(config_file, checkpoint_file, device=device)

# test a single video and show the result:
video = 'demo/demo.mp4'
labels = 'demo/label_map_construction.txt'
results = inference_recognizer(model, video, labels)

# show the results
print(f'The top-5 labels with corresponding scores are:')
for result in results:
    print(f'{result[0]}: ', result[1])

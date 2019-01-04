from tensorboardX import SummaryWriter
import numpy as np

writer = SummaryWriter()
for i in range(0,10):
    dummy_img = np.random.random([1, 3, 256, 256])  # output from network
    writer.add_image('Image', dummy_img, i)


writer.export_scalars_to_json("./all_scalars_2.json")
writer.close()


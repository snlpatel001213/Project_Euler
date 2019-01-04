from tensorboardX import SummaryWriter
import numpy as np

writer = SummaryWriter()
i = [np.random.randint(0,100) for i in range(0,32)]
writer.add_embedding(np.random.random([32,20]), i)


writer.export_scalars_to_json("./all_scalars_2.json")
writer.close()

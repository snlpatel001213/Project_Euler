from tensorboardX import SummaryWriter
import math
import random

writer = SummaryWriter()

# writing both to separately
for i in range(0,100):
    writer.add_scalar('sin',math.sin(i*0.001) + random.random(), i)
    writer.add_scalar('cos', math.cos(i*0.001) + random.random(), i)

writer.export_scalars_to_json("./all_scalars.json")
writer.close()


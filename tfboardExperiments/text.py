from tensorboardX import SummaryWriter
import numpy as np

writer = SummaryWriter()
for i in range(0,10):
    writer.add_text('mytext', 'this is a pen_'+str(i), i)


writer.export_scalars_to_json("./all_scalars_2.json")
writer.close()


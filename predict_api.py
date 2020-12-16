from __future__ import absolute_import

import logging

import tensorflow as tf

from aocr.model.model import Model
from aocr.defaults import Config

def get_init_model(model_dir="pretrained/checkpoints"):
	sess = tf.Session(config=tf.ConfigProto(allow_soft_placement=True))
	model = Model(
		phase="predict",
		visualize=Config.VISUALIZE,
		output_dir=Config.OUTPUT_DIR,
		batch_size=1,
		initial_learning_rate=Config.INITIAL_LEARNING_RATE,
		steps_per_checkpoint=Config.STEPS_PER_CHECKPOINT,
		model_dir=model_dir,
		target_embedding_size=Config.TARGET_EMBEDDING_SIZE,
		attn_num_hidden=Config.ATTN_NUM_HIDDEN,
		attn_num_layers=Config.ATTN_NUM_LAYERS,
		clip_gradients=Config.CLIP_GRADIENTS,
		max_gradient_norm=Config.MAX_GRADIENT_NORM,
		session=sess,
		load_model=Config.LOAD_MODEL,
		gpu_id=Config.GPU_ID,
		use_gru=Config.USE_GRU,
		use_distance=Config.USE_DISTANCE,
		max_image_width=Config.MAX_WIDTH,
		max_image_height=Config.MAX_HEIGHT,
		max_prediction_length=Config.MAX_PREDICTION,
		channels=Config.CHANNELS,
	)
	return model

def predict(input_image_path, model):
	try:
		with open(input_image_path, 'rb') as img_file:
			img_file_data = img_file.read()
	except IOError:
		logging.error('Result: error while opening file %s.', input_image_path)
		return "ERROR: Error while opening file"
	text, probability = model.predict(img_file_data)
	logging.info('Result: OK. %s %s', '{:.2f}'.format(probability), text)

	return text

def main():
	print("RAN FROM MAIN")

if __name__ == '__main__':
	main()

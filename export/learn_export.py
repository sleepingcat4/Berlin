# Export the fine-tuned model as a TensorFlow SavedModel
export_module_dir = os.path.join(os.getcwd(), "finetuned_yamnet_export")
tf.saved_model.save(model, export_module_dir)
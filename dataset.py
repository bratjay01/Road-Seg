import torch.utils.data
import cv2
import os
import numpy as np

class SearchDataset(torch.utils.data.Dataset):

    CLASSES = ['sky', 'building', 'pole', 'road', 'pavement', 
               'tree', 'signsymbol', 'fence', 'car', 
               'pedestrian', 'bicyclist', 'unlabelled']
    
    def __init__(
            self, 
            images_dir, 
            masks_dir, 
            classes=None, 
            augmentation=None, 
            preprocessing=None,
    ):
        self.ids = os.listdir(images_dir)
        self.images_fps = [os.path.join(images_dir, image_id) for image_id in self.ids]
        self.masks_fps = [os.path.join(masks_dir, image_id) for image_id in self.ids]
        
        self.classes = classes if classes is not None else self.CLASSES
        self.num_classes = len(self.classes) + 1  # Add 1 for the "background" class
        
        # Define the index of the "road" class
        self.road_class_idx = self.classes.index('road')
        
        self.augmentation = augmentation
        self.preprocessing = preprocessing

    def __getitem__(self, i):
        # Read data
        image = cv2.imread(self.images_fps[i])
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        mask = cv2.imread(self.masks_fps[i], 0)
        
        # Initialize the multi-class mask
        output_mask = np.zeros((image.shape[0], image.shape[1], self.num_classes), dtype=np.float32)
        
        # Map class IDs to their respective positions in the output mask
        for class_idx, class_name in enumerate(self.classes):
            class_mask = (mask == class_idx)
            output_mask[..., class_idx] = class_mask
        
        # Create the "road" class as the last class in the mask
        road_mask = (mask == self.road_class_idx)
        output_mask[..., -1] = road_mask
        
        # Apply augmentations
        if self.augmentation:
            augmented = self.augmentation(image=image, mask=output_mask)
            image, output_mask = augmented['image'], augmented['mask']
        
        # Apply preprocessing
        if self.preprocessing:
            preprocessed = self.preprocessing(image=image, mask=output_mask)
            image, output_mask = preprocessed['image'], preprocessed['mask']
            
        return image, output_mask
        
    def __len__(self):
        return len(self.ids)
    
    
    # def __init__(self, transform=None):
    #     self.transform = transform
    #     # Implement additional initialization logic if needed

    # def __len__(self):
    #     # Replace `...` with the actual implementation
    #     ...

    # def __getitem__(self, index):
    #     # Implement logic to get an image and its mask using the received index.
    #     #
    #     # `image` should be a NumPy array with the shape [height, width, num_channels].
    #     # If an image contains three color channels, it should use an RGB color scheme.
    #     #
    #     # `mask` should be a NumPy array with the shape [height, width, num_classes] where `num_classes`
    #     # is a value set in the `search.yaml` file. Each mask channel should encode values for a single class (usually
    #     # pixel in that channel has a value of 1.0 if the corresponding pixel from the image belongs to this class and
    #     # 0.0 otherwise). During augmentation search, `nn.BCEWithLogitsLoss` is used as a segmentation loss.

    #     image = ...
    #     mask = ...

    #     if self.transform is not None:
    #         transformed = self.transform(image=image, mask=mask)
    #         image = transformed["image"]
    #         mask = transformed["mask"]
    #     return image, mask

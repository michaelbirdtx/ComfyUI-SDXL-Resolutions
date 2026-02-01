class ImageResolutions:
    """
    A custom node for selecting turbo-optimized image resolutions
    """
    
    # Resolution mappings with all ratio options

    RESOLUTIONS = {
        "1024": [
            "1024x1024 (1:1)",
            "1152x896 (9:7)",
            "896x1152 (7:9)",
            "1280x960 (4:3)",
            "960x1280 (3:4)",
            "1216x832 (19:13)",
            "832x1216 (13:19)",
            "1344x768 (7:4)",
            "768x1344 (4:7)",
            "1344x576 (7:3)",
            "576x1344 (3:7)"
        ],
        "1280": [
            "1280x1280 (1:1)",
            "1472x1152 (23:18)",
            "1152x1472 (18:23)",
            "1536x1152 (4:3)",
            "1152x1536 (3:4)",
            "1536x1024 (3:2)",
            "1024x1536 (2:3)",
            "1792x1024 (7:4)",
            "1024x1792 (4:7)",
            "1792x768 (7:3)",
            "768x1792 (3:7)"
        ],
        "1536": [
            "1536x1536 (1:1)",
            "1728x1344 (9:7)",
            "1344x1728 (7:9)",
            "1792x1344 (4:3)",
            "1344x1792 (3:4)",
            "1920x1280 (3:2)",
            "1280x1920 (2:3)",
            "2048x1152 (16:9)",
            "1152x2048 (9:16)",
            "2240x960 (7:3)",
            "960x2240 (3:7)"
        ],
        "PonyXL Optimized": [
            "1024x1024 (1:1)",
            "1152x896 (9:7)",
            "896x1152 (7:9)",
            "1152x864 (4:3)",
            "864x1152 (3:4)",
            "1216x832 (19:13)",
            "832x1216 (13:19)",
            "1344x768 (7:4)",
            "768x1344 (4:7)",
            "1344x576 (7:3)",
            "576x1344 (3:7)"
        ],
        "ZIT Optimized": [
            "1024x1024 (1:1)",
            "832x1216 (portrait, ~13:19)",
            "1216x832 (landscape, ~19:13)",
            "768x1152 (portrait)",
            "1152x768 (landscape)",
            "896x1344 (vertical, text-first)",
            "1344x896 (horizontal, text-first)",
            "1152x648 (16:9 approx, thumbnails)",
            "648x1152 (9:16 approx)",
            "1216x684 (16:9, YouTube-style)"
        ]
    }

    @classmethod
    def INPUT_TYPES(cls):
        # Get all resolution options
        resolution_options = list(cls.RESOLUTIONS.keys())
        
        # Get all ratio options (we'll show all, but filter in JS if needed)
        all_ratios = []
        for ratios in cls.RESOLUTIONS.values():
            all_ratios.extend(ratios)
        # Remove duplicates while preserving order
        all_ratios = list(dict.fromkeys(all_ratios))
        
        return {
            "required": {
                "resolution": (resolution_options, {"default": "1024"}),
                "ratio": (all_ratios, {"default": "1024x1024 (1:1)"}),
            },
        }
    
    RETURN_TYPES = ("INT", "INT", "INT")
    RETURN_NAMES = ("resolution", "width", "height")
    FUNCTION = "get_dimensions"
    CATEGORY = "image/resolution"
    
    def get_dimensions(self, resolution, ratio):
        """
        Parse the selected resolution and ratio to return dimensions
        """
        # Extract width and height from the ratio string (format: "1024x1024 (1:1)")
        dimensions = ratio.split(" ")[0]  # Get "1024x1024" part
        width, height = dimensions.split("x")
        
        # Convert to integers
        resolution_int = int(resolution)
        width_int = int(width)
        height_int = int(height)
        
        return (resolution_int, width_int, height_int)


# Node registration
NODE_CLASS_MAPPINGS = {
    "ImageResolutions": ImageResolutions
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ImageResolutions": "Image Resolutions"
}

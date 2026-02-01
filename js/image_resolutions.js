import { app } from "../../scripts/app.js";

// Resolution mappings
const RESOLUTIONS = {
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
        "1344x576 (21:9)",
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
    ]
};

app.registerExtension({
    name: "ImageResolutions",
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (nodeData.name === "ImageResolutions") {
            const onNodeCreated = nodeType.prototype.onNodeCreated;
            
            nodeType.prototype.onNodeCreated = function() {
                const result = onNodeCreated?.apply(this, arguments);
                
                const resolutionWidget = this.widgets.find(w => w.name === "resolution");
                const ratioWidget = this.widgets.find(w => w.name === "ratio");
                
                if (resolutionWidget && ratioWidget) {
                    // Function to update ratio options based on resolution
                    const updateRatioOptions = (resolution) => {
                        const ratios = RESOLUTIONS[resolution] || [];
                        ratioWidget.options.values = ratios;
                        
                        // If current ratio is not in the new list, reset to first option
                        if (!ratios.includes(ratioWidget.value)) {
                            ratioWidget.value = ratios[0];
                        }
                    };
                    
                    // Store original callback
                    const originalCallback = resolutionWidget.callback;
                    
                    // Override resolution widget callback
                    resolutionWidget.callback = function(value) {
                        updateRatioOptions(value);
                        if (originalCallback) {
                            originalCallback.apply(this, arguments);
                        }
                    };
                    
                    // Initialize with current resolution
                    updateRatioOptions(resolutionWidget.value);
                }
                
                return result;
            };
        }
    }
});

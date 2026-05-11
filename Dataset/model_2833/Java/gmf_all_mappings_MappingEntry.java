





import java.util.List;
import java.util.ArrayList;

public class gmf_all_mappings_MappingEntry  {






    private List<VisualEffectMapping> visualeffectmappings;




    private List<CanvasMapping> canvasmappings;


    public gmf_all_mappings_MappingEntry(
    ) {
        this.visualeffectmappings = new ArrayList<>();
        this.canvasmappings = new ArrayList<>();
    }

    public gmf_all_mappings_MappingEntry(
        ArrayList<VisualEffectMapping> visualeffectmappings,        ArrayList<CanvasMapping> canvasmappings    ) {
        this.visualeffectmappings = visualeffectmappings;
        this.canvasmappings = canvasmappings;
    }


    public List<VisualEffectMapping> getVisualeffectmappings() {
        return visualeffectmappings;
    }

    public void addVisualeffectmapping(Visualeffectmapping visualeffectmapping) {
        this.visualeffectmappings.add(visualeffectmapping);
    }
    public List<CanvasMapping> getCanvasmappings() {
        return canvasmappings;
    }

    public void addCanvasmapping(Canvasmapping canvasmapping) {
        this.canvasmappings.add(canvasmapping);
    }

}
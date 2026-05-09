





import java.util.List;
import java.util.ArrayList;

public class UnifiedMetamodel__Layer  {

    private String name;





    private List<UnifiedMetamodel__LayerSegment> unifiedmetamodel__layersegments;


    public UnifiedMetamodel__Layer(
        String name    ) {
        this.name = name;
        this.unifiedmetamodel__layersegments = new ArrayList<>();
    }

    public UnifiedMetamodel__Layer(
        String name        ArrayList<UnifiedMetamodel__LayerSegment> unifiedmetamodel__layersegments    ) {
        this.name = name;
        this.unifiedmetamodel__layersegments = unifiedmetamodel__layersegments;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<UnifiedMetamodel__LayerSegment> getUnifiedmetamodel__layersegments() {
        return unifiedmetamodel__layersegments;
    }

    public void addUnifiedmetamodel__layersegment(Unifiedmetamodel__layersegment unifiedmetamodel__layersegment) {
        this.unifiedmetamodel__layersegments.add(unifiedmetamodel__layersegment);
    }

}






import java.util.List;
import java.util.ArrayList;

public class dsl_LayerSegmentRelation  {

    private String layerSegment;





    private dsl_LayerSegment dsl_layersegment;


    public dsl_LayerSegmentRelation(
        String layerSegment    ) {
        this.layerSegment = layerSegment;
    }


    public String getLayersegment() {
        return layerSegment;
    }

    public void setLayersegment(String layerSegment) {
        this.layerSegment = layerSegment;
    }

    public dsl_LayerSegment getDsl_layersegment() {
        return dsl_layersegment;
    }

    public void setDsl_layersegment(dsl_LayerSegment dsl_layersegment) {
        this.dsl_layersegment = dsl_layersegment;
    }

}
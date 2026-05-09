





import java.util.List;
import java.util.ArrayList;

public class myDsl_LayerSegmentRelation  {

    private String layerSegment;





    private myDsl_LayerSegment mydsl_layersegment;


    public myDsl_LayerSegmentRelation(
        String layerSegment    ) {
        this.layerSegment = layerSegment;
    }


    public String getLayersegment() {
        return layerSegment;
    }

    public void setLayersegment(String layerSegment) {
        this.layerSegment = layerSegment;
    }

    public myDsl_LayerSegment getMydsl_layersegment() {
        return mydsl_layersegment;
    }

    public void setMydsl_layersegment(myDsl_LayerSegment mydsl_layersegment) {
        this.mydsl_layersegment = mydsl_layersegment;
    }

}
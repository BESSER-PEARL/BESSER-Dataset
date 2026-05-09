





import java.util.List;
import java.util.ArrayList;

public class dsl_SublayerSegment  {

    private String name;





    private dsl_LayerSegment dsl_layersegment;


    public dsl_SublayerSegment(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dsl_LayerSegment getDsl_layersegment() {
        return dsl_layersegment;
    }

    public void setDsl_layersegment(dsl_LayerSegment dsl_layersegment) {
        this.dsl_layersegment = dsl_layersegment;
    }

}
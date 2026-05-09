





import java.util.List;
import java.util.ArrayList;

public class myDsl_SublayerSegment  {

    private String name;





    private myDsl_LayerSegment mydsl_layersegment;


    public myDsl_SublayerSegment(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDsl_LayerSegment getMydsl_layersegment() {
        return mydsl_layersegment;
    }

    public void setMydsl_layersegment(myDsl_LayerSegment mydsl_layersegment) {
        this.mydsl_layersegment = mydsl_layersegment;
    }

}
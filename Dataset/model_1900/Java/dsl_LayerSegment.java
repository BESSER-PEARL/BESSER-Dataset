





import java.util.List;
import java.util.ArrayList;

public class dsl_LayerSegment  {

    private String name;





    private dsl_Layer dsl_layer;


    public dsl_LayerSegment(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dsl_Layer getDsl_layer() {
        return dsl_layer;
    }

    public void setDsl_layer(dsl_Layer dsl_layer) {
        this.dsl_layer = dsl_layer;
    }

}
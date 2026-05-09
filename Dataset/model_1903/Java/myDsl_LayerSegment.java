





import java.util.List;
import java.util.ArrayList;

public class myDsl_LayerSegment  {

    private String name;





    private myDsl_Layer mydsl_layer;


    public myDsl_LayerSegment(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDsl_Layer getMydsl_layer() {
        return mydsl_layer;
    }

    public void setMydsl_layer(myDsl_Layer mydsl_layer) {
        this.mydsl_layer = mydsl_layer;
    }

}
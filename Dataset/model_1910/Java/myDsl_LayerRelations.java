





import java.util.List;
import java.util.ArrayList;

public class myDsl_LayerRelations  {

    private String name;
    private String layerelations;



    public myDsl_LayerRelations(
        String name,        String layerelations    ) {
        this.name = name;
        this.layerelations = layerelations;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getLayerelations() {
        return layerelations;
    }

    public void setLayerelations(String layerelations) {
        this.layerelations = layerelations;
    }


}
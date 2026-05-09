





import java.util.List;
import java.util.ArrayList;

public class myDsl_LayerSource  {

    private String layerelations;





    private myDsl_LayerRelations mydsl_layerrelations;


    public myDsl_LayerSource(
        String layerelations    ) {
        this.layerelations = layerelations;
    }


    public String getLayerelations() {
        return layerelations;
    }

    public void setLayerelations(String layerelations) {
        this.layerelations = layerelations;
    }

    public myDsl_LayerRelations getMydsl_layerrelations() {
        return mydsl_layerrelations;
    }

    public void setMydsl_layerrelations(myDsl_LayerRelations mydsl_layerrelations) {
        this.mydsl_layerrelations = mydsl_layerrelations;
    }

}
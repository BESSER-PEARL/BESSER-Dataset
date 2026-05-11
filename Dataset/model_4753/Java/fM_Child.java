





import java.util.List;
import java.util.ArrayList;

public class fM_Child  {

    private String name;
    private boolean mandatory;





    private fM_Node fm_node;




    private fM_FeatureDiagram fm_featurediagram;


    public fM_Child(
        String name,        boolean mandatory    ) {
        this.name = name;
        this.mandatory = mandatory;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getMandatory() {
        return mandatory;
    }

    public void setMandatory(boolean mandatory) {
        this.mandatory = mandatory;
    }

    public fM_Node getFm_node() {
        return fm_node;
    }

    public void setFm_node(fM_Node fm_node) {
        this.fm_node = fm_node;
    }
    public fM_FeatureDiagram getFm_featurediagram() {
        return fm_featurediagram;
    }

    public void setFm_featurediagram(fM_FeatureDiagram fm_featurediagram) {
        this.fm_featurediagram = fm_featurediagram;
    }

}
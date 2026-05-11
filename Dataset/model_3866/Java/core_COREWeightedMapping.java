





import java.util.List;
import java.util.ArrayList;

public class core_COREWeightedMapping  {

    private int weight;





    private core_COREFeatureImpactNode core_corefeatureimpactnode;


    public core_COREWeightedMapping(
        int weight    ) {
        this.weight = weight;
    }


    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }

    public core_COREFeatureImpactNode getCore_corefeatureimpactnode() {
        return core_corefeatureimpactnode;
    }

    public void setCore_corefeatureimpactnode(core_COREFeatureImpactNode core_corefeatureimpactnode) {
        this.core_corefeatureimpactnode = core_corefeatureimpactnode;
    }

}
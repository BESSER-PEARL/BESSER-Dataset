





import java.util.List;
import java.util.ArrayList;

public class core_COREFeatureImpactNode extends COREImpactNode {

    private int relativeFeatureWeight;





    private core_COREFeature core_corefeature;


    public core_COREFeatureImpactNode(
        int relativeFeatureWeight    ) {
        super(
        );
        this.relativeFeatureWeight = relativeFeatureWeight;
    }


    public int getRelativefeatureweight() {
        return relativeFeatureWeight;
    }

    public void setRelativefeatureweight(int relativeFeatureWeight) {
        this.relativeFeatureWeight = relativeFeatureWeight;
    }

    public core_COREFeature getCore_corefeature() {
        return core_corefeature;
    }

    public void setCore_corefeature(core_COREFeature core_corefeature) {
        this.core_corefeature = core_corefeature;
    }

}
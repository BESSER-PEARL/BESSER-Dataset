





import java.util.List;
import java.util.ArrayList;

public class core_COREFeatureImpact extends COREImpactModelElement {

    private float relativeFeatureWeight;





    private core_COREFeature core_corefeature;


    public core_COREFeatureImpact(
        float relativeFeatureWeight    ) {
        super(
        );
        this.relativeFeatureWeight = relativeFeatureWeight;
    }


    public float getRelativefeatureweight() {
        return relativeFeatureWeight;
    }

    public void setRelativefeatureweight(float relativeFeatureWeight) {
        this.relativeFeatureWeight = relativeFeatureWeight;
    }

    public core_COREFeature getCore_corefeature() {
        return core_corefeature;
    }

    public void setCore_corefeature(core_COREFeature core_corefeature) {
        this.core_corefeature = core_corefeature;
    }

}
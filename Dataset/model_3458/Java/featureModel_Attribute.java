





import java.util.List;
import java.util.ArrayList;

public class featureModel_Attribute extends VariabilityElement {

    private boolean runtime;
    private String name;





    private featureModel_Feature featuremodel_feature;


    public featureModel_Attribute(
        boolean runtime,        String name    ) {
        super(
        );
        this.runtime = runtime;
        this.name = name;
    }


    public boolean getRuntime() {
        return runtime;
    }

    public void setRuntime(boolean runtime) {
        this.runtime = runtime;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public featureModel_Feature getFeaturemodel_feature() {
        return featuremodel_feature;
    }

    public void setFeaturemodel_feature(featureModel_Feature featuremodel_feature) {
        this.featuremodel_feature = featuremodel_feature;
    }

}
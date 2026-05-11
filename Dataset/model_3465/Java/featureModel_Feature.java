





import java.util.List;
import java.util.ArrayList;

public class featureModel_Feature extends Group {

    private String name;





    private featureModel_FeatureModel featuremodel_featuremodel;


    public featureModel_Feature(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public featureModel_FeatureModel getFeaturemodel_featuremodel() {
        return featuremodel_featuremodel;
    }

    public void setFeaturemodel_featuremodel(featureModel_FeatureModel featuremodel_featuremodel) {
        this.featuremodel_featuremodel = featuremodel_featuremodel;
    }

}
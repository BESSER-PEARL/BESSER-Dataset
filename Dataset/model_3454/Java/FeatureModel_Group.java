





import java.util.List;
import java.util.ArrayList;

public class FeatureModel_Group extends NamedElement {

    private String groupType;





    private FeatureModel_FeatureModel featuremodel_featuremodel;


    public FeatureModel_Group(
        String groupType    ) {
        super(
        );
        this.groupType = groupType;
    }


    public String getGrouptype() {
        return groupType;
    }

    public void setGrouptype(String groupType) {
        this.groupType = groupType;
    }

    public FeatureModel_FeatureModel getFeaturemodel_featuremodel() {
        return featuremodel_featuremodel;
    }

    public void setFeaturemodel_featuremodel(FeatureModel_FeatureModel featuremodel_featuremodel) {
        this.featuremodel_featuremodel = featuremodel_featuremodel;
    }

}
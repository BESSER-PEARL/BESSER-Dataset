





import java.util.List;
import java.util.ArrayList;

public class FeatureModel_ConfigConstraint extends Constraint {

    private String kind;





    private FeatureModel_RootFeature featuremodel_rootfeature;


    public FeatureModel_ConfigConstraint(
        String kind    ) {
        super(
        );
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public FeatureModel_RootFeature getFeaturemodel_rootfeature() {
        return featuremodel_rootfeature;
    }

    public void setFeaturemodel_rootfeature(FeatureModel_RootFeature featuremodel_rootfeature) {
        this.featuremodel_rootfeature = featuremodel_rootfeature;
    }

}
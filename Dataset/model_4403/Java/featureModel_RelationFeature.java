





import java.util.List;
import java.util.ArrayList;

public class featureModel_RelationFeature extends Relation {

    private int lowerBound;
    private String type;
    private int upperBound;





    private featureModel_Feature featuremodel_feature;




    private featureModel_Feature featuremodel_feature;


    public featureModel_RelationFeature(
        int lowerBound,        String type,        int upperBound    ) {
        super(
        );
        this.lowerBound = lowerBound;
        this.type = type;
        this.upperBound = upperBound;
    }


    public int getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(int lowerBound) {
        this.lowerBound = lowerBound;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public int getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(int upperBound) {
        this.upperBound = upperBound;
    }

    public featureModel_Feature getFeaturemodel_feature() {
        return featuremodel_feature;
    }

    public void setFeaturemodel_feature(featureModel_Feature featuremodel_feature) {
        this.featuremodel_feature = featuremodel_feature;
    }
    public featureModel_Feature getFeaturemodel_feature() {
        return featuremodel_feature;
    }

    public void setFeaturemodel_feature(featureModel_Feature featuremodel_feature) {
        this.featuremodel_feature = featuremodel_feature;
    }

}
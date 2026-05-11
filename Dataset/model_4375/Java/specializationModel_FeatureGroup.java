





import java.util.List;
import java.util.ArrayList;

public class specializationModel_FeatureGroup extends Node {

    private int lowerBound;
    private String type;
    private int upperBound;





    private List<specializationModel_Feature> specializationmodel_features;


    public specializationModel_FeatureGroup(
        int lowerBound,        String type,        int upperBound    ) {
        super(
        );
        this.lowerBound = lowerBound;
        this.type = type;
        this.upperBound = upperBound;
        this.specializationmodel_features = new ArrayList<>();
    }

    public specializationModel_FeatureGroup(
        int lowerBound,        String type,        int upperBound        ArrayList<specializationModel_Feature> specializationmodel_features    ) {
        this.lowerBound = lowerBound;
        this.type = type;
        this.upperBound = upperBound;
        this.specializationmodel_features = specializationmodel_features;
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

    public List<specializationModel_Feature> getSpecializationmodel_features() {
        return specializationmodel_features;
    }

    public void addSpecializationmodel_feature(Specializationmodel_feature specializationmodel_feature) {
        this.specializationmodel_features.add(specializationmodel_feature);
    }

}
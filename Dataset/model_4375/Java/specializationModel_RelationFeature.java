





import java.util.List;
import java.util.ArrayList;

public class specializationModel_RelationFeature extends Relation {

    private int upperBound;
    private String type;
    private int lowerBound;





    private specializationModel_Feature specializationmodel_feature;




    private specializationModel_Feature specializationmodel_feature;


    public specializationModel_RelationFeature(
        int upperBound,        String type,        int lowerBound    ) {
        super(
        );
        this.upperBound = upperBound;
        this.type = type;
        this.lowerBound = lowerBound;
    }


    public int getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(int upperBound) {
        this.upperBound = upperBound;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public int getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(int lowerBound) {
        this.lowerBound = lowerBound;
    }

    public specializationModel_Feature getSpecializationmodel_feature() {
        return specializationmodel_feature;
    }

    public void setSpecializationmodel_feature(specializationModel_Feature specializationmodel_feature) {
        this.specializationmodel_feature = specializationmodel_feature;
    }
    public specializationModel_Feature getSpecializationmodel_feature() {
        return specializationmodel_feature;
    }

    public void setSpecializationmodel_feature(specializationModel_Feature specializationmodel_feature) {
        this.specializationmodel_feature = specializationmodel_feature;
    }

}
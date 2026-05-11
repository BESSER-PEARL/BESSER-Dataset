





import java.util.List;
import java.util.ArrayList;

public class feature_Feature  {

    private String name;
    private int maxCardinality;
    private int minCardinality;





    private feature_FeatureModel feature_featuremodel;




    private List<feature_Constraint> feature_constraints;




    private feature_Constraint feature_constraint;


    public feature_Feature(
        String name,        int maxCardinality,        int minCardinality    ) {
        this.name = name;
        this.maxCardinality = maxCardinality;
        this.minCardinality = minCardinality;
        this.feature_constraints = new ArrayList<>();
    }

    public feature_Feature(
        String name,        int maxCardinality,        int minCardinality        ArrayList<feature_Constraint> feature_constraints    ) {
        this.name = name;
        this.maxCardinality = maxCardinality;
        this.minCardinality = minCardinality;
        this.feature_constraints = feature_constraints;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getMaxcardinality() {
        return maxCardinality;
    }

    public void setMaxcardinality(int maxCardinality) {
        this.maxCardinality = maxCardinality;
    }
    public int getMincardinality() {
        return minCardinality;
    }

    public void setMincardinality(int minCardinality) {
        this.minCardinality = minCardinality;
    }

    public feature_FeatureModel getFeature_featuremodel() {
        return feature_featuremodel;
    }

    public void setFeature_featuremodel(feature_FeatureModel feature_featuremodel) {
        this.feature_featuremodel = feature_featuremodel;
    }
    public List<feature_Constraint> getFeature_constraints() {
        return feature_constraints;
    }

    public void addFeature_constraint(Feature_constraint feature_constraint) {
        this.feature_constraints.add(feature_constraint);
    }
    public feature_Constraint getFeature_constraint() {
        return feature_constraint;
    }

    public void setFeature_constraint(feature_Constraint feature_constraint) {
        this.feature_constraint = feature_constraint;
    }

}
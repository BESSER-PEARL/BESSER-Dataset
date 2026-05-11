





import java.util.List;
import java.util.ArrayList;

public class feature_FeatureModel  {

    private String name;





    private List<feature_Domain> feature_domains;




    private List<feature_Constraint> feature_constraints;




    private feature_Feature feature_feature;


    public feature_FeatureModel(
        String name    ) {
        this.name = name;
        this.feature_domains = new ArrayList<>();
        this.feature_constraints = new ArrayList<>();
    }

    public feature_FeatureModel(
        String name        ArrayList<feature_Domain> feature_domains,        ArrayList<feature_Constraint> feature_constraints    ) {
        this.name = name;
        this.feature_domains = feature_domains;
        this.feature_constraints = feature_constraints;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<feature_Domain> getFeature_domains() {
        return feature_domains;
    }

    public void addFeature_domain(Feature_domain feature_domain) {
        this.feature_domains.add(feature_domain);
    }
    public List<feature_Constraint> getFeature_constraints() {
        return feature_constraints;
    }

    public void addFeature_constraint(Feature_constraint feature_constraint) {
        this.feature_constraints.add(feature_constraint);
    }
    public feature_Feature getFeature_feature() {
        return feature_feature;
    }

    public void setFeature_feature(feature_Feature feature_feature) {
        this.feature_feature = feature_feature;
    }

}
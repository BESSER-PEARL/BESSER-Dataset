





import java.util.List;
import java.util.ArrayList;

public class feature_Feature extends FeatureTreeNode {

    private String name;





    private List<feature_Constraint> feature_constraints;




    private feature_Constraint feature_constraint;


    public feature_Feature(
        String name    ) {
        super(
        );
        this.name = name;
        this.feature_constraints = new ArrayList<>();
    }

    public feature_Feature(
        String name        ArrayList<feature_Constraint> feature_constraints    ) {
        this.name = name;
        this.feature_constraints = feature_constraints;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
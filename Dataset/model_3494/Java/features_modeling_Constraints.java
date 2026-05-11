





import java.util.List;
import java.util.ArrayList;

public class features_modeling_Constraints  {






    private List<features_modeling_Constraint> features_modeling_constraints;


    public features_modeling_Constraints(
    ) {
        this.features_modeling_constraints = new ArrayList<>();
    }

    public features_modeling_Constraints(
        ArrayList<features_modeling_Constraint> features_modeling_constraints    ) {
        this.features_modeling_constraints = features_modeling_constraints;
    }


    public List<features_modeling_Constraint> getFeatures_modeling_constraints() {
        return features_modeling_constraints;
    }

    public void addFeatures_modeling_constraint(Features_modeling_constraint features_modeling_constraint) {
        this.features_modeling_constraints.add(features_modeling_constraint);
    }

}
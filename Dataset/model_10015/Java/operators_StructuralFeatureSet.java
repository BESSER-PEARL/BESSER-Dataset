





import java.util.List;
import java.util.ArrayList;

public class operators_StructuralFeatureSet  {






    private List<operators_EStructuralFeature> operators_estructuralfeatures;




    private operators_SPLIT operators_split;


    public operators_StructuralFeatureSet(
    ) {
        this.operators_estructuralfeatures = new ArrayList<>();
    }

    public operators_StructuralFeatureSet(
        ArrayList<operators_EStructuralFeature> operators_estructuralfeatures    ) {
        this.operators_estructuralfeatures = operators_estructuralfeatures;
    }


    public List<operators_EStructuralFeature> getOperators_estructuralfeatures() {
        return operators_estructuralfeatures;
    }

    public void addOperators_estructuralfeature(Operators_estructuralfeature operators_estructuralfeature) {
        this.operators_estructuralfeatures.add(operators_estructuralfeature);
    }
    public operators_SPLIT getOperators_split() {
        return operators_split;
    }

    public void setOperators_split(operators_SPLIT operators_split) {
        this.operators_split = operators_split;
    }

}
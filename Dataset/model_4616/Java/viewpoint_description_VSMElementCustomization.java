





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_VSMElementCustomization extends IVSMElementCustomization {

    private String predicateExpression;





    private List<EStructuralFeatureCustomization> estructuralfeaturecustomizations;


    public viewpoint_description_VSMElementCustomization(
        String predicateExpression    ) {
        super(
        );
        this.predicateExpression = predicateExpression;
        this.estructuralfeaturecustomizations = new ArrayList<>();
    }

    public viewpoint_description_VSMElementCustomization(
        String predicateExpression        ArrayList<EStructuralFeatureCustomization> estructuralfeaturecustomizations    ) {
        this.predicateExpression = predicateExpression;
        this.estructuralfeaturecustomizations = estructuralfeaturecustomizations;
    }

    public String getPredicateexpression() {
        return predicateExpression;
    }

    public void setPredicateexpression(String predicateExpression) {
        this.predicateExpression = predicateExpression;
    }

    public List<EStructuralFeatureCustomization> getEstructuralfeaturecustomizations() {
        return estructuralfeaturecustomizations;
    }

    public void addEstructuralfeaturecustomization(Estructuralfeaturecustomization estructuralfeaturecustomization) {
        this.estructuralfeaturecustomizations.add(estructuralfeaturecustomization);
    }

}
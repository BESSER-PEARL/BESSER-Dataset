





import java.util.List;
import java.util.ArrayList;

public class RefinementsEcore_EOperation extends ETypedElement {






    private RefinementsEcore_EClass refinementsecore_eclass;




    private RefinementsEcore_EClass refinementsecore_eclass;




    private List<RefinementsEcore_EClassifier> refinementsecore_eclassifiers;


    public RefinementsEcore_EOperation(
    ) {
        super(
        );
        this.refinementsecore_eclassifiers = new ArrayList<>();
    }

    public RefinementsEcore_EOperation(
        ArrayList<RefinementsEcore_EClassifier> refinementsecore_eclassifiers    ) {
        this.refinementsecore_eclassifiers = refinementsecore_eclassifiers;
    }


    public RefinementsEcore_EClass getRefinementsecore_eclass() {
        return refinementsecore_eclass;
    }

    public void setRefinementsecore_eclass(RefinementsEcore_EClass refinementsecore_eclass) {
        this.refinementsecore_eclass = refinementsecore_eclass;
    }
    public RefinementsEcore_EClass getRefinementsecore_eclass() {
        return refinementsecore_eclass;
    }

    public void setRefinementsecore_eclass(RefinementsEcore_EClass refinementsecore_eclass) {
        this.refinementsecore_eclass = refinementsecore_eclass;
    }
    public List<RefinementsEcore_EClassifier> getRefinementsecore_eclassifiers() {
        return refinementsecore_eclassifiers;
    }

    public void addRefinementsecore_eclassifier(Refinementsecore_eclassifier refinementsecore_eclassifier) {
        this.refinementsecore_eclassifiers.add(refinementsecore_eclassifier);
    }

}
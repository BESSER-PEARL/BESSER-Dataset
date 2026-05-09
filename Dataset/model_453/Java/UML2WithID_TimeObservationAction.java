





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_TimeObservationAction extends WriteStructuralFeatureAction {






    private List<UML2WithID_TimeExpression> uml2withid_timeexpressions;


    public UML2WithID_TimeObservationAction(
    ) {
        super(
        );
        this.uml2withid_timeexpressions = new ArrayList<>();
    }

    public UML2WithID_TimeObservationAction(
        ArrayList<UML2WithID_TimeExpression> uml2withid_timeexpressions    ) {
        this.uml2withid_timeexpressions = uml2withid_timeexpressions;
    }


    public List<UML2WithID_TimeExpression> getUml2withid_timeexpressions() {
        return uml2withid_timeexpressions;
    }

    public void addUml2withid_timeexpression(Uml2withid_timeexpression uml2withid_timeexpression) {
        this.uml2withid_timeexpressions.add(uml2withid_timeexpression);
    }

}






import java.util.List;
import java.util.ArrayList;

public class UML2_TimeObservationAction extends WriteStructuralFeatureAction {






    private List<UML2_TimeExpression> uml2_timeexpressions;


    public UML2_TimeObservationAction(
    ) {
        super(
        );
        this.uml2_timeexpressions = new ArrayList<>();
    }

    public UML2_TimeObservationAction(
        ArrayList<UML2_TimeExpression> uml2_timeexpressions    ) {
        this.uml2_timeexpressions = uml2_timeexpressions;
    }


    public List<UML2_TimeExpression> getUml2_timeexpressions() {
        return uml2_timeexpressions;
    }

    public void addUml2_timeexpression(Uml2_timeexpression uml2_timeexpression) {
        this.uml2_timeexpressions.add(uml2_timeexpression);
    }

}
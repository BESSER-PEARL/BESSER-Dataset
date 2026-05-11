





import java.util.List;
import java.util.ArrayList;

public class altarica_Transition  {






    private altarica_Event altarica_event;




    private List<altarica_Affectation> altarica_affectations;




    private altarica_AbstractExpression altarica_abstractexpression;




    private altarica_TransitionSpecification altarica_transitionspecification;


    public altarica_Transition(
    ) {
        this.altarica_affectations = new ArrayList<>();
    }

    public altarica_Transition(
        ArrayList<altarica_Affectation> altarica_affectations    ) {
        this.altarica_affectations = altarica_affectations;
    }


    public altarica_Event getAltarica_event() {
        return altarica_event;
    }

    public void setAltarica_event(altarica_Event altarica_event) {
        this.altarica_event = altarica_event;
    }
    public List<altarica_Affectation> getAltarica_affectations() {
        return altarica_affectations;
    }

    public void addAltarica_affectation(Altarica_affectation altarica_affectation) {
        this.altarica_affectations.add(altarica_affectation);
    }
    public altarica_AbstractExpression getAltarica_abstractexpression() {
        return altarica_abstractexpression;
    }

    public void setAltarica_abstractexpression(altarica_AbstractExpression altarica_abstractexpression) {
        this.altarica_abstractexpression = altarica_abstractexpression;
    }
    public altarica_TransitionSpecification getAltarica_transitionspecification() {
        return altarica_transitionspecification;
    }

    public void setAltarica_transitionspecification(altarica_TransitionSpecification altarica_transitionspecification) {
        this.altarica_transitionspecification = altarica_transitionspecification;
    }

}
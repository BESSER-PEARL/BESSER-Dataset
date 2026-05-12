





import java.util.List;
import java.util.ArrayList;

public class UML2_Action extends ExecutableNode {

    private String effect;





    private UML2_Activity uml2_activity;




    private UML2_Classifier uml2_classifier;




    private List<UML2_Constraint> uml2_constraints;




    private List<UML2_Constraint> uml2_constraints;


    public UML2_Action(
        String effect    ) {
        super(
        );
        this.effect = effect;
        this.uml2_constraints = new ArrayList<>();
        this.uml2_constraints = new ArrayList<>();
    }

    public UML2_Action(
        String effect        ArrayList<UML2_Constraint> uml2_constraints,        ArrayList<UML2_Constraint> uml2_constraints    ) {
        this.effect = effect;
        this.uml2_constraints = uml2_constraints;
        this.uml2_constraints = uml2_constraints;
    }

    public String getEffect() {
        return effect;
    }

    public void setEffect(String effect) {
        this.effect = effect;
    }

    public UML2_Activity getUml2_activity() {
        return uml2_activity;
    }

    public void setUml2_activity(UML2_Activity uml2_activity) {
        this.uml2_activity = uml2_activity;
    }
    public UML2_Classifier getUml2_classifier() {
        return uml2_classifier;
    }

    public void setUml2_classifier(UML2_Classifier uml2_classifier) {
        this.uml2_classifier = uml2_classifier;
    }
    public List<UML2_Constraint> getUml2_constraints() {
        return uml2_constraints;
    }

    public void addUml2_constraint(Uml2_constraint uml2_constraint) {
        this.uml2_constraints.add(uml2_constraint);
    }
    public List<UML2_Constraint> getUml2_constraints() {
        return uml2_constraints;
    }

    public void addUml2_constraint(Uml2_constraint uml2_constraint) {
        this.uml2_constraints.add(uml2_constraint);
    }

}
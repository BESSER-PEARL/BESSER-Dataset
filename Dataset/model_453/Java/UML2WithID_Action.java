





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Action extends ExecutableNode {

    private String effect;





    private List<UML2WithID_Constraint> uml2withid_constraints;




    private UML2WithID_Activity uml2withid_activity;




    private UML2WithID_Classifier uml2withid_classifier;




    private List<UML2WithID_Constraint> uml2withid_constraints;


    public UML2WithID_Action(
        String effect    ) {
        super(
        );
        this.effect = effect;
        this.uml2withid_constraints = new ArrayList<>();
        this.uml2withid_constraints = new ArrayList<>();
    }

    public UML2WithID_Action(
        String effect        ArrayList<UML2WithID_Constraint> uml2withid_constraints,        ArrayList<UML2WithID_Constraint> uml2withid_constraints    ) {
        this.effect = effect;
        this.uml2withid_constraints = uml2withid_constraints;
        this.uml2withid_constraints = uml2withid_constraints;
    }

    public String getEffect() {
        return effect;
    }

    public void setEffect(String effect) {
        this.effect = effect;
    }

    public List<UML2WithID_Constraint> getUml2withid_constraints() {
        return uml2withid_constraints;
    }

    public void addUml2withid_constraint(Uml2withid_constraint uml2withid_constraint) {
        this.uml2withid_constraints.add(uml2withid_constraint);
    }
    public UML2WithID_Activity getUml2withid_activity() {
        return uml2withid_activity;
    }

    public void setUml2withid_activity(UML2WithID_Activity uml2withid_activity) {
        this.uml2withid_activity = uml2withid_activity;
    }
    public UML2WithID_Classifier getUml2withid_classifier() {
        return uml2withid_classifier;
    }

    public void setUml2withid_classifier(UML2WithID_Classifier uml2withid_classifier) {
        this.uml2withid_classifier = uml2withid_classifier;
    }
    public List<UML2WithID_Constraint> getUml2withid_constraints() {
        return uml2withid_constraints;
    }

    public void addUml2withid_constraint(Uml2withid_constraint uml2withid_constraint) {
        this.uml2withid_constraints.add(uml2withid_constraint);
    }

}
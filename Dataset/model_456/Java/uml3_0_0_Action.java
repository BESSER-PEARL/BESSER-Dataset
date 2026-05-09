





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_Action extends ExecutableNode {






    private List<uml3_0_0_Constraint> uml3_0_0_constraints;




    private List<uml3_0_0_OutputPin> uml3_0_0_outputpins;




    private uml3_0_0_Interaction uml3_0_0_interaction;




    private uml3_0_0_ActionExecutionSpecification uml3_0_0_actionexecutionspecification;




    private uml3_0_0_Classifier uml3_0_0_classifier;




    private uml3_0_0_InteractionUse uml3_0_0_interactionuse;




    private uml3_0_0_ActionInputPin uml3_0_0_actioninputpin;




    private List<uml3_0_0_InputPin> uml3_0_0_inputpins;




    private List<uml3_0_0_Constraint> uml3_0_0_constraints;


    public uml3_0_0_Action(
    ) {
        super(
        );
        this.uml3_0_0_constraints = new ArrayList<>();
        this.uml3_0_0_outputpins = new ArrayList<>();
        this.uml3_0_0_inputpins = new ArrayList<>();
        this.uml3_0_0_constraints = new ArrayList<>();
    }

    public uml3_0_0_Action(
        ArrayList<uml3_0_0_Constraint> uml3_0_0_constraints,        ArrayList<uml3_0_0_OutputPin> uml3_0_0_outputpins,        ArrayList<uml3_0_0_InputPin> uml3_0_0_inputpins,        ArrayList<uml3_0_0_Constraint> uml3_0_0_constraints    ) {
        this.uml3_0_0_constraints = uml3_0_0_constraints;
        this.uml3_0_0_outputpins = uml3_0_0_outputpins;
        this.uml3_0_0_inputpins = uml3_0_0_inputpins;
        this.uml3_0_0_constraints = uml3_0_0_constraints;
    }


    public List<uml3_0_0_Constraint> getUml3_0_0_constraints() {
        return uml3_0_0_constraints;
    }

    public void addUml3_0_0_constraint(Uml3_0_0_constraint uml3_0_0_constraint) {
        this.uml3_0_0_constraints.add(uml3_0_0_constraint);
    }
    public List<uml3_0_0_OutputPin> getUml3_0_0_outputpins() {
        return uml3_0_0_outputpins;
    }

    public void addUml3_0_0_outputpin(Uml3_0_0_outputpin uml3_0_0_outputpin) {
        this.uml3_0_0_outputpins.add(uml3_0_0_outputpin);
    }
    public uml3_0_0_Interaction getUml3_0_0_interaction() {
        return uml3_0_0_interaction;
    }

    public void setUml3_0_0_interaction(uml3_0_0_Interaction uml3_0_0_interaction) {
        this.uml3_0_0_interaction = uml3_0_0_interaction;
    }
    public uml3_0_0_ActionExecutionSpecification getUml3_0_0_actionexecutionspecification() {
        return uml3_0_0_actionexecutionspecification;
    }

    public void setUml3_0_0_actionexecutionspecification(uml3_0_0_ActionExecutionSpecification uml3_0_0_actionexecutionspecification) {
        this.uml3_0_0_actionexecutionspecification = uml3_0_0_actionexecutionspecification;
    }
    public uml3_0_0_Classifier getUml3_0_0_classifier() {
        return uml3_0_0_classifier;
    }

    public void setUml3_0_0_classifier(uml3_0_0_Classifier uml3_0_0_classifier) {
        this.uml3_0_0_classifier = uml3_0_0_classifier;
    }
    public uml3_0_0_InteractionUse getUml3_0_0_interactionuse() {
        return uml3_0_0_interactionuse;
    }

    public void setUml3_0_0_interactionuse(uml3_0_0_InteractionUse uml3_0_0_interactionuse) {
        this.uml3_0_0_interactionuse = uml3_0_0_interactionuse;
    }
    public uml3_0_0_ActionInputPin getUml3_0_0_actioninputpin() {
        return uml3_0_0_actioninputpin;
    }

    public void setUml3_0_0_actioninputpin(uml3_0_0_ActionInputPin uml3_0_0_actioninputpin) {
        this.uml3_0_0_actioninputpin = uml3_0_0_actioninputpin;
    }
    public List<uml3_0_0_InputPin> getUml3_0_0_inputpins() {
        return uml3_0_0_inputpins;
    }

    public void addUml3_0_0_inputpin(Uml3_0_0_inputpin uml3_0_0_inputpin) {
        this.uml3_0_0_inputpins.add(uml3_0_0_inputpin);
    }
    public List<uml3_0_0_Constraint> getUml3_0_0_constraints() {
        return uml3_0_0_constraints;
    }

    public void addUml3_0_0_constraint(Uml3_0_0_constraint uml3_0_0_constraint) {
        this.uml3_0_0_constraints.add(uml3_0_0_constraint);
    }

}
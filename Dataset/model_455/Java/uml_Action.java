





import java.util.List;
import java.util.ArrayList;

public class uml_Action extends ExecutableNode {






    private List<uml_InputPin> uml_inputpins;




    private List<uml_OutputPin> uml_outputpins;




    private uml_Interaction uml_interaction;




    private uml_Classifier uml_classifier;




    private List<uml_Constraint> uml_constraints;




    private List<uml_Constraint> uml_constraints;


    public uml_Action(
    ) {
        super(
        );
        this.uml_inputpins = new ArrayList<>();
        this.uml_outputpins = new ArrayList<>();
        this.uml_constraints = new ArrayList<>();
        this.uml_constraints = new ArrayList<>();
    }

    public uml_Action(
        ArrayList<uml_InputPin> uml_inputpins,        ArrayList<uml_OutputPin> uml_outputpins,        ArrayList<uml_Constraint> uml_constraints,        ArrayList<uml_Constraint> uml_constraints    ) {
        this.uml_inputpins = uml_inputpins;
        this.uml_outputpins = uml_outputpins;
        this.uml_constraints = uml_constraints;
        this.uml_constraints = uml_constraints;
    }


    public List<uml_InputPin> getUml_inputpins() {
        return uml_inputpins;
    }

    public void addUml_inputpin(Uml_inputpin uml_inputpin) {
        this.uml_inputpins.add(uml_inputpin);
    }
    public List<uml_OutputPin> getUml_outputpins() {
        return uml_outputpins;
    }

    public void addUml_outputpin(Uml_outputpin uml_outputpin) {
        this.uml_outputpins.add(uml_outputpin);
    }
    public uml_Interaction getUml_interaction() {
        return uml_interaction;
    }

    public void setUml_interaction(uml_Interaction uml_interaction) {
        this.uml_interaction = uml_interaction;
    }
    public uml_Classifier getUml_classifier() {
        return uml_classifier;
    }

    public void setUml_classifier(uml_Classifier uml_classifier) {
        this.uml_classifier = uml_classifier;
    }
    public List<uml_Constraint> getUml_constraints() {
        return uml_constraints;
    }

    public void addUml_constraint(Uml_constraint uml_constraint) {
        this.uml_constraints.add(uml_constraint);
    }
    public List<uml_Constraint> getUml_constraints() {
        return uml_constraints;
    }

    public void addUml_constraint(Uml_constraint uml_constraint) {
        this.uml_constraints.add(uml_constraint);
    }

}
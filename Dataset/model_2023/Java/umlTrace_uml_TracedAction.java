





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedAction extends TracedExecutableNode {






    private uml_TracedClassifier uml_tracedclassifier;




    private List<uml_TracedInputPin> uml_tracedinputpins;




    private List<uml_TracedConstraint> uml_tracedconstraints;




    private List<uml_TracedConstraint> uml_tracedconstraints;




    private List<uml_TracedOutputPin> uml_tracedoutputpins;


    public umlTrace_uml_TracedAction(
    ) {
        super(
        );
        this.uml_tracedinputpins = new ArrayList<>();
        this.uml_tracedconstraints = new ArrayList<>();
        this.uml_tracedconstraints = new ArrayList<>();
        this.uml_tracedoutputpins = new ArrayList<>();
    }

    public umlTrace_uml_TracedAction(
        ArrayList<uml_TracedInputPin> uml_tracedinputpins,        ArrayList<uml_TracedConstraint> uml_tracedconstraints,        ArrayList<uml_TracedConstraint> uml_tracedconstraints,        ArrayList<uml_TracedOutputPin> uml_tracedoutputpins    ) {
        this.uml_tracedinputpins = uml_tracedinputpins;
        this.uml_tracedconstraints = uml_tracedconstraints;
        this.uml_tracedconstraints = uml_tracedconstraints;
        this.uml_tracedoutputpins = uml_tracedoutputpins;
    }


    public uml_TracedClassifier getUml_tracedclassifier() {
        return uml_tracedclassifier;
    }

    public void setUml_tracedclassifier(uml_TracedClassifier uml_tracedclassifier) {
        this.uml_tracedclassifier = uml_tracedclassifier;
    }
    public List<uml_TracedInputPin> getUml_tracedinputpins() {
        return uml_tracedinputpins;
    }

    public void addUml_tracedinputpin(Uml_tracedinputpin uml_tracedinputpin) {
        this.uml_tracedinputpins.add(uml_tracedinputpin);
    }
    public List<uml_TracedConstraint> getUml_tracedconstraints() {
        return uml_tracedconstraints;
    }

    public void addUml_tracedconstraint(Uml_tracedconstraint uml_tracedconstraint) {
        this.uml_tracedconstraints.add(uml_tracedconstraint);
    }
    public List<uml_TracedConstraint> getUml_tracedconstraints() {
        return uml_tracedconstraints;
    }

    public void addUml_tracedconstraint(Uml_tracedconstraint uml_tracedconstraint) {
        this.uml_tracedconstraints.add(uml_tracedconstraint);
    }
    public List<uml_TracedOutputPin> getUml_tracedoutputpins() {
        return uml_tracedoutputpins;
    }

    public void addUml_tracedoutputpin(Uml_tracedoutputpin uml_tracedoutputpin) {
        this.uml_tracedoutputpins.add(uml_tracedoutputpin);
    }

}
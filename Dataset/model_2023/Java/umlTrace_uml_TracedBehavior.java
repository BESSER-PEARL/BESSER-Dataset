





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedBehavior extends TracedClass {






    private List<uml_TracedConstraint> uml_tracedconstraints;




    private uml_TracedBehavioredClassifier uml_tracedbehavioredclassifier;




    private List<uml_TracedConstraint> uml_tracedconstraints;




    private List<uml_TracedParameterSet> uml_tracedparametersets;




    private List<uml_TracedParameter> uml_tracedparameters;


    public umlTrace_uml_TracedBehavior(
    ) {
        super(
        );
        this.uml_tracedconstraints = new ArrayList<>();
        this.uml_tracedconstraints = new ArrayList<>();
        this.uml_tracedparametersets = new ArrayList<>();
        this.uml_tracedparameters = new ArrayList<>();
    }

    public umlTrace_uml_TracedBehavior(
        ArrayList<uml_TracedConstraint> uml_tracedconstraints,        ArrayList<uml_TracedConstraint> uml_tracedconstraints,        ArrayList<uml_TracedParameterSet> uml_tracedparametersets,        ArrayList<uml_TracedParameter> uml_tracedparameters    ) {
        this.uml_tracedconstraints = uml_tracedconstraints;
        this.uml_tracedconstraints = uml_tracedconstraints;
        this.uml_tracedparametersets = uml_tracedparametersets;
        this.uml_tracedparameters = uml_tracedparameters;
    }


    public List<uml_TracedConstraint> getUml_tracedconstraints() {
        return uml_tracedconstraints;
    }

    public void addUml_tracedconstraint(Uml_tracedconstraint uml_tracedconstraint) {
        this.uml_tracedconstraints.add(uml_tracedconstraint);
    }
    public uml_TracedBehavioredClassifier getUml_tracedbehavioredclassifier() {
        return uml_tracedbehavioredclassifier;
    }

    public void setUml_tracedbehavioredclassifier(uml_TracedBehavioredClassifier uml_tracedbehavioredclassifier) {
        this.uml_tracedbehavioredclassifier = uml_tracedbehavioredclassifier;
    }
    public List<uml_TracedConstraint> getUml_tracedconstraints() {
        return uml_tracedconstraints;
    }

    public void addUml_tracedconstraint(Uml_tracedconstraint uml_tracedconstraint) {
        this.uml_tracedconstraints.add(uml_tracedconstraint);
    }
    public List<uml_TracedParameterSet> getUml_tracedparametersets() {
        return uml_tracedparametersets;
    }

    public void addUml_tracedparameterset(Uml_tracedparameterset uml_tracedparameterset) {
        this.uml_tracedparametersets.add(uml_tracedparameterset);
    }
    public List<uml_TracedParameter> getUml_tracedparameters() {
        return uml_tracedparameters;
    }

    public void addUml_tracedparameter(Uml_tracedparameter uml_tracedparameter) {
        this.uml_tracedparameters.add(uml_tracedparameter);
    }

}
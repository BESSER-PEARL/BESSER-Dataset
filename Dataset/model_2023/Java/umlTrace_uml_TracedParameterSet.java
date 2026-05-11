





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedParameterSet extends TracedNamedElement {






    private List<uml_TracedConstraint> uml_tracedconstraints;




    private List<uml_TracedParameter> uml_tracedparameters;


    public umlTrace_uml_TracedParameterSet(
    ) {
        super(
        );
        this.uml_tracedconstraints = new ArrayList<>();
        this.uml_tracedparameters = new ArrayList<>();
    }

    public umlTrace_uml_TracedParameterSet(
        ArrayList<uml_TracedConstraint> uml_tracedconstraints,        ArrayList<uml_TracedParameter> uml_tracedparameters    ) {
        this.uml_tracedconstraints = uml_tracedconstraints;
        this.uml_tracedparameters = uml_tracedparameters;
    }


    public List<uml_TracedConstraint> getUml_tracedconstraints() {
        return uml_tracedconstraints;
    }

    public void addUml_tracedconstraint(Uml_tracedconstraint uml_tracedconstraint) {
        this.uml_tracedconstraints.add(uml_tracedconstraint);
    }
    public List<uml_TracedParameter> getUml_tracedparameters() {
        return uml_tracedparameters;
    }

    public void addUml_tracedparameter(Uml_tracedparameter uml_tracedparameter) {
        this.uml_tracedparameters.add(uml_tracedparameter);
    }

}
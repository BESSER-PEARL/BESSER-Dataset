





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedBehavioralFeature extends uml_TracedFeature, uml_TracedNamespace {






    private List<uml_TracedParameter> uml_tracedparameters;




    private List<uml_TracedParameterSet> uml_tracedparametersets;


    public umlTrace_uml_TracedBehavioralFeature(
    ) {
        super(
        );
        this.uml_tracedparameters = new ArrayList<>();
        this.uml_tracedparametersets = new ArrayList<>();
    }

    public umlTrace_uml_TracedBehavioralFeature(
        ArrayList<uml_TracedParameter> uml_tracedparameters,        ArrayList<uml_TracedParameterSet> uml_tracedparametersets    ) {
        this.uml_tracedparameters = uml_tracedparameters;
        this.uml_tracedparametersets = uml_tracedparametersets;
    }


    public List<uml_TracedParameter> getUml_tracedparameters() {
        return uml_tracedparameters;
    }

    public void addUml_tracedparameter(Uml_tracedparameter uml_tracedparameter) {
        this.uml_tracedparameters.add(uml_tracedparameter);
    }
    public List<uml_TracedParameterSet> getUml_tracedparametersets() {
        return uml_tracedparametersets;
    }

    public void addUml_tracedparameterset(Uml_tracedparameterset uml_tracedparameterset) {
        this.uml_tracedparametersets.add(uml_tracedparameterset);
    }

}
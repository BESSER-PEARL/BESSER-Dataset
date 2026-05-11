





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedParameter extends uml_TracedConnectableElement, uml_TracedMultiplicityElement {






    private uml_TracedValueSpecification uml_tracedvaluespecification;




    private uml_TracedOperation uml_tracedoperation;




    private List<uml_TracedParameterSet> uml_tracedparametersets;


    public umlTrace_uml_TracedParameter(
    ) {
        super(
        );
        this.uml_tracedparametersets = new ArrayList<>();
    }

    public umlTrace_uml_TracedParameter(
        ArrayList<uml_TracedParameterSet> uml_tracedparametersets    ) {
        this.uml_tracedparametersets = uml_tracedparametersets;
    }


    public uml_TracedValueSpecification getUml_tracedvaluespecification() {
        return uml_tracedvaluespecification;
    }

    public void setUml_tracedvaluespecification(uml_TracedValueSpecification uml_tracedvaluespecification) {
        this.uml_tracedvaluespecification = uml_tracedvaluespecification;
    }
    public uml_TracedOperation getUml_tracedoperation() {
        return uml_tracedoperation;
    }

    public void setUml_tracedoperation(uml_TracedOperation uml_tracedoperation) {
        this.uml_tracedoperation = uml_tracedoperation;
    }
    public List<uml_TracedParameterSet> getUml_tracedparametersets() {
        return uml_tracedparametersets;
    }

    public void addUml_tracedparameterset(Uml_tracedparameterset uml_tracedparameterset) {
        this.uml_tracedparametersets.add(uml_tracedparameterset);
    }

}
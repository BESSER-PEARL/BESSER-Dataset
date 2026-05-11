





import java.util.List;
import java.util.ArrayList;

public class UML2_Behavior  {






    private List<UML2_ParameterSet> uml2_parametersets;




    private UML2_OpaqueExpression uml2_opaqueexpression;


    public UML2_Behavior(
    ) {
        this.uml2_parametersets = new ArrayList<>();
    }

    public UML2_Behavior(
        ArrayList<UML2_ParameterSet> uml2_parametersets    ) {
        this.uml2_parametersets = uml2_parametersets;
    }


    public List<UML2_ParameterSet> getUml2_parametersets() {
        return uml2_parametersets;
    }

    public void addUml2_parameterset(Uml2_parameterset uml2_parameterset) {
        this.uml2_parametersets.add(uml2_parameterset);
    }
    public UML2_OpaqueExpression getUml2_opaqueexpression() {
        return uml2_opaqueexpression;
    }

    public void setUml2_opaqueexpression(UML2_OpaqueExpression uml2_opaqueexpression) {
        this.uml2_opaqueexpression = uml2_opaqueexpression;
    }

}
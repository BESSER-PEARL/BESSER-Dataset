





import java.util.List;
import java.util.ArrayList;

public class UML2_Parameter extends MultiplicityElement, ConnectableElement, TypedElement {

    private String direction;
    private String effect;
    private boolean isException;
    private String default;
    private boolean isStream;





    private UML2_OpaqueExpression uml2_opaqueexpression;




    private List<UML2_ParameterSet> uml2_parametersets;




    private UML2_ParameterSet uml2_parameterset;


    public UML2_Parameter(
        String direction,        String effect,        boolean isException,        String default,        boolean isStream    ) {
        super(
        );
        this.direction = direction;
        this.effect = effect;
        this.isException = isException;
        this.default = default;
        this.isStream = isStream;
        this.uml2_parametersets = new ArrayList<>();
    }

    public UML2_Parameter(
        String direction,        String effect,        boolean isException,        String default,        boolean isStream        ArrayList<UML2_ParameterSet> uml2_parametersets    ) {
        this.direction = direction;
        this.effect = effect;
        this.isException = isException;
        this.default = default;
        this.isStream = isStream;
        this.uml2_parametersets = uml2_parametersets;
    }

    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
    public String getEffect() {
        return effect;
    }

    public void setEffect(String effect) {
        this.effect = effect;
    }
    public boolean getIsexception() {
        return isException;
    }

    public void setIsexception(boolean isException) {
        this.isException = isException;
    }
    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }
    public boolean getIsstream() {
        return isStream;
    }

    public void setIsstream(boolean isStream) {
        this.isStream = isStream;
    }

    public UML2_OpaqueExpression getUml2_opaqueexpression() {
        return uml2_opaqueexpression;
    }

    public void setUml2_opaqueexpression(UML2_OpaqueExpression uml2_opaqueexpression) {
        this.uml2_opaqueexpression = uml2_opaqueexpression;
    }
    public List<UML2_ParameterSet> getUml2_parametersets() {
        return uml2_parametersets;
    }

    public void addUml2_parameterset(Uml2_parameterset uml2_parameterset) {
        this.uml2_parametersets.add(uml2_parameterset);
    }
    public UML2_ParameterSet getUml2_parameterset() {
        return uml2_parameterset;
    }

    public void setUml2_parameterset(UML2_ParameterSet uml2_parameterset) {
        this.uml2_parameterset = uml2_parameterset;
    }

}
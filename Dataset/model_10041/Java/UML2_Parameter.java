





import java.util.List;
import java.util.ArrayList;

public class UML2_Parameter extends MultiplicityElement, TypedElement, ConnectableElement {

    private boolean isException;
    private String default;
    private String effect;
    private String direction;
    private boolean isStream;





    private UML2_OpaqueExpression uml2_opaqueexpression;




    private UML2_ValueSpecification uml2_valuespecification;




    private UML2_ParameterSet uml2_parameterset;




    private List<UML2_ParameterSet> uml2_parametersets;


    public UML2_Parameter(
        boolean isException,        String default,        String effect,        String direction,        boolean isStream    ) {
        super(
        );
        this.isException = isException;
        this.default = default;
        this.effect = effect;
        this.direction = direction;
        this.isStream = isStream;
        this.uml2_parametersets = new ArrayList<>();
    }

    public UML2_Parameter(
        boolean isException,        String default,        String effect,        String direction,        boolean isStream        ArrayList<UML2_ParameterSet> uml2_parametersets    ) {
        this.isException = isException;
        this.default = default;
        this.effect = effect;
        this.direction = direction;
        this.isStream = isStream;
        this.uml2_parametersets = uml2_parametersets;
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
    public String getEffect() {
        return effect;
    }

    public void setEffect(String effect) {
        this.effect = effect;
    }
    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
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
    public UML2_ValueSpecification getUml2_valuespecification() {
        return uml2_valuespecification;
    }

    public void setUml2_valuespecification(UML2_ValueSpecification uml2_valuespecification) {
        this.uml2_valuespecification = uml2_valuespecification;
    }
    public UML2_ParameterSet getUml2_parameterset() {
        return uml2_parameterset;
    }

    public void setUml2_parameterset(UML2_ParameterSet uml2_parameterset) {
        this.uml2_parameterset = uml2_parameterset;
    }
    public List<UML2_ParameterSet> getUml2_parametersets() {
        return uml2_parametersets;
    }

    public void addUml2_parameterset(Uml2_parameterset uml2_parameterset) {
        this.uml2_parametersets.add(uml2_parameterset);
    }

}
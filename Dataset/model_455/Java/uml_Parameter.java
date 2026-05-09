





import java.util.List;
import java.util.ArrayList;

public class uml_Parameter extends MultiplicityElement, ConnectableElement {

    private String direction;
    private String default;
    private String effect;
    private String isStream;
    private String isException;





    private uml_OpaqueExpression uml_opaqueexpression;




    private uml_Operation uml_operation;




    private uml_BehavioralFeature uml_behavioralfeature;




    private List<uml_ParameterSet> uml_parametersets;




    private uml_ValueSpecification uml_valuespecification;




    private uml_ParameterSet uml_parameterset;


    public uml_Parameter(
        String direction,        String default,        String effect,        String isStream,        String isException    ) {
        super(
        );
        this.direction = direction;
        this.default = default;
        this.effect = effect;
        this.isStream = isStream;
        this.isException = isException;
        this.uml_parametersets = new ArrayList<>();
    }

    public uml_Parameter(
        String direction,        String default,        String effect,        String isStream,        String isException        ArrayList<uml_ParameterSet> uml_parametersets    ) {
        this.direction = direction;
        this.default = default;
        this.effect = effect;
        this.isStream = isStream;
        this.isException = isException;
        this.uml_parametersets = uml_parametersets;
    }

    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
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
    public String getIsstream() {
        return isStream;
    }

    public void setIsstream(String isStream) {
        this.isStream = isStream;
    }
    public String getIsexception() {
        return isException;
    }

    public void setIsexception(String isException) {
        this.isException = isException;
    }

    public uml_OpaqueExpression getUml_opaqueexpression() {
        return uml_opaqueexpression;
    }

    public void setUml_opaqueexpression(uml_OpaqueExpression uml_opaqueexpression) {
        this.uml_opaqueexpression = uml_opaqueexpression;
    }
    public uml_Operation getUml_operation() {
        return uml_operation;
    }

    public void setUml_operation(uml_Operation uml_operation) {
        this.uml_operation = uml_operation;
    }
    public uml_BehavioralFeature getUml_behavioralfeature() {
        return uml_behavioralfeature;
    }

    public void setUml_behavioralfeature(uml_BehavioralFeature uml_behavioralfeature) {
        this.uml_behavioralfeature = uml_behavioralfeature;
    }
    public List<uml_ParameterSet> getUml_parametersets() {
        return uml_parametersets;
    }

    public void addUml_parameterset(Uml_parameterset uml_parameterset) {
        this.uml_parametersets.add(uml_parameterset);
    }
    public uml_ValueSpecification getUml_valuespecification() {
        return uml_valuespecification;
    }

    public void setUml_valuespecification(uml_ValueSpecification uml_valuespecification) {
        this.uml_valuespecification = uml_valuespecification;
    }
    public uml_ParameterSet getUml_parameterset() {
        return uml_parameterset;
    }

    public void setUml_parameterset(uml_ParameterSet uml_parameterset) {
        this.uml_parameterset = uml_parameterset;
    }

}






import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_Parameter extends ConnectableElement, MultiplicityElement {

    private String isStream;
    private String default;
    private String direction;
    private String isException;
    private String effect;





    private uml3_0_0_BehavioralFeature uml3_0_0_behavioralfeature;




    private uml3_0_0_ValueSpecification uml3_0_0_valuespecification;




    private List<uml3_0_0_ParameterSet> uml3_0_0_parametersets;




    private uml3_0_0_Operation uml3_0_0_operation;




    private uml3_0_0_ParameterSet uml3_0_0_parameterset;


    public uml3_0_0_Parameter(
        String isStream,        String default,        String direction,        String isException,        String effect    ) {
        super(
        );
        this.isStream = isStream;
        this.default = default;
        this.direction = direction;
        this.isException = isException;
        this.effect = effect;
        this.uml3_0_0_parametersets = new ArrayList<>();
    }

    public uml3_0_0_Parameter(
        String isStream,        String default,        String direction,        String isException,        String effect        ArrayList<uml3_0_0_ParameterSet> uml3_0_0_parametersets    ) {
        this.isStream = isStream;
        this.default = default;
        this.direction = direction;
        this.isException = isException;
        this.effect = effect;
        this.uml3_0_0_parametersets = uml3_0_0_parametersets;
    }

    public String getIsstream() {
        return isStream;
    }

    public void setIsstream(String isStream) {
        this.isStream = isStream;
    }
    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }
    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
    public String getIsexception() {
        return isException;
    }

    public void setIsexception(String isException) {
        this.isException = isException;
    }
    public String getEffect() {
        return effect;
    }

    public void setEffect(String effect) {
        this.effect = effect;
    }

    public uml3_0_0_BehavioralFeature getUml3_0_0_behavioralfeature() {
        return uml3_0_0_behavioralfeature;
    }

    public void setUml3_0_0_behavioralfeature(uml3_0_0_BehavioralFeature uml3_0_0_behavioralfeature) {
        this.uml3_0_0_behavioralfeature = uml3_0_0_behavioralfeature;
    }
    public uml3_0_0_ValueSpecification getUml3_0_0_valuespecification() {
        return uml3_0_0_valuespecification;
    }

    public void setUml3_0_0_valuespecification(uml3_0_0_ValueSpecification uml3_0_0_valuespecification) {
        this.uml3_0_0_valuespecification = uml3_0_0_valuespecification;
    }
    public List<uml3_0_0_ParameterSet> getUml3_0_0_parametersets() {
        return uml3_0_0_parametersets;
    }

    public void addUml3_0_0_parameterset(Uml3_0_0_parameterset uml3_0_0_parameterset) {
        this.uml3_0_0_parametersets.add(uml3_0_0_parameterset);
    }
    public uml3_0_0_Operation getUml3_0_0_operation() {
        return uml3_0_0_operation;
    }

    public void setUml3_0_0_operation(uml3_0_0_Operation uml3_0_0_operation) {
        this.uml3_0_0_operation = uml3_0_0_operation;
    }
    public uml3_0_0_ParameterSet getUml3_0_0_parameterset() {
        return uml3_0_0_parameterset;
    }

    public void setUml3_0_0_parameterset(uml3_0_0_ParameterSet uml3_0_0_parameterset) {
        this.uml3_0_0_parameterset = uml3_0_0_parameterset;
    }

}
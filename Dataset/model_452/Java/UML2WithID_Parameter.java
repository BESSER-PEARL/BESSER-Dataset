





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Parameter extends TypedElement, MultiplicityElement, ConnectableElement {

    private boolean isStream;
    private boolean isException;
    private String default;
    private String direction;
    private String effect;





    private UML2WithID_ParameterSet uml2withid_parameterset;




    private UML2WithID_Behavior uml2withid_behavior;




    private UML2WithID_BehavioralFeature uml2withid_behavioralfeature;




    private UML2WithID_Behavior uml2withid_behavior;




    private UML2WithID_BehavioralFeature uml2withid_behavioralfeature;




    private UML2WithID_Behavior uml2withid_behavior;




    private List<UML2WithID_ParameterSet> uml2withid_parametersets;




    private UML2WithID_ValueSpecification uml2withid_valuespecification;




    private UML2WithID_BehavioralFeature uml2withid_behavioralfeature;


    public UML2WithID_Parameter(
        boolean isStream,        boolean isException,        String default,        String direction,        String effect    ) {
        super(
        );
        this.isStream = isStream;
        this.isException = isException;
        this.default = default;
        this.direction = direction;
        this.effect = effect;
        this.uml2withid_parametersets = new ArrayList<>();
    }

    public UML2WithID_Parameter(
        boolean isStream,        boolean isException,        String default,        String direction,        String effect        ArrayList<UML2WithID_ParameterSet> uml2withid_parametersets    ) {
        this.isStream = isStream;
        this.isException = isException;
        this.default = default;
        this.direction = direction;
        this.effect = effect;
        this.uml2withid_parametersets = uml2withid_parametersets;
    }

    public boolean getIsstream() {
        return isStream;
    }

    public void setIsstream(boolean isStream) {
        this.isStream = isStream;
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

    public UML2WithID_ParameterSet getUml2withid_parameterset() {
        return uml2withid_parameterset;
    }

    public void setUml2withid_parameterset(UML2WithID_ParameterSet uml2withid_parameterset) {
        this.uml2withid_parameterset = uml2withid_parameterset;
    }
    public UML2WithID_Behavior getUml2withid_behavior() {
        return uml2withid_behavior;
    }

    public void setUml2withid_behavior(UML2WithID_Behavior uml2withid_behavior) {
        this.uml2withid_behavior = uml2withid_behavior;
    }
    public UML2WithID_BehavioralFeature getUml2withid_behavioralfeature() {
        return uml2withid_behavioralfeature;
    }

    public void setUml2withid_behavioralfeature(UML2WithID_BehavioralFeature uml2withid_behavioralfeature) {
        this.uml2withid_behavioralfeature = uml2withid_behavioralfeature;
    }
    public UML2WithID_Behavior getUml2withid_behavior() {
        return uml2withid_behavior;
    }

    public void setUml2withid_behavior(UML2WithID_Behavior uml2withid_behavior) {
        this.uml2withid_behavior = uml2withid_behavior;
    }
    public UML2WithID_BehavioralFeature getUml2withid_behavioralfeature() {
        return uml2withid_behavioralfeature;
    }

    public void setUml2withid_behavioralfeature(UML2WithID_BehavioralFeature uml2withid_behavioralfeature) {
        this.uml2withid_behavioralfeature = uml2withid_behavioralfeature;
    }
    public UML2WithID_Behavior getUml2withid_behavior() {
        return uml2withid_behavior;
    }

    public void setUml2withid_behavior(UML2WithID_Behavior uml2withid_behavior) {
        this.uml2withid_behavior = uml2withid_behavior;
    }
    public List<UML2WithID_ParameterSet> getUml2withid_parametersets() {
        return uml2withid_parametersets;
    }

    public void addUml2withid_parameterset(Uml2withid_parameterset uml2withid_parameterset) {
        this.uml2withid_parametersets.add(uml2withid_parameterset);
    }
    public UML2WithID_ValueSpecification getUml2withid_valuespecification() {
        return uml2withid_valuespecification;
    }

    public void setUml2withid_valuespecification(UML2WithID_ValueSpecification uml2withid_valuespecification) {
        this.uml2withid_valuespecification = uml2withid_valuespecification;
    }
    public UML2WithID_BehavioralFeature getUml2withid_behavioralfeature() {
        return uml2withid_behavioralfeature;
    }

    public void setUml2withid_behavioralfeature(UML2WithID_BehavioralFeature uml2withid_behavioralfeature) {
        this.uml2withid_behavioralfeature = uml2withid_behavioralfeature;
    }

}
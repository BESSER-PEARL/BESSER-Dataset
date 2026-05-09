





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Behavior extends Class {

    private boolean isReentrant;





    private UML2WithID_BehavioralFeature uml2withid_behavioralfeature;




    private UML2WithID_Connector uml2withid_connector;




    private UML2WithID_BehavioralFeature uml2withid_behavioralfeature;




    private UML2WithID_BehavioredClassifier uml2withid_behavioredclassifier;




    private UML2WithID_BehavioredClassifier uml2withid_behavioredclassifier;




    private List<UML2WithID_ParameterSet> uml2withid_parametersets;




    private UML2WithID_Behavior uml2withid_behavior;




    private UML2WithID_BehavioredClassifier uml2withid_behavioredclassifier;


    public UML2WithID_Behavior(
        boolean isReentrant    ) {
        super(
        );
        this.isReentrant = isReentrant;
        this.uml2withid_parametersets = new ArrayList<>();
    }

    public UML2WithID_Behavior(
        boolean isReentrant        ArrayList<UML2WithID_ParameterSet> uml2withid_parametersets    ) {
        this.isReentrant = isReentrant;
        this.uml2withid_parametersets = uml2withid_parametersets;
    }

    public boolean getIsreentrant() {
        return isReentrant;
    }

    public void setIsreentrant(boolean isReentrant) {
        this.isReentrant = isReentrant;
    }

    public UML2WithID_BehavioralFeature getUml2withid_behavioralfeature() {
        return uml2withid_behavioralfeature;
    }

    public void setUml2withid_behavioralfeature(UML2WithID_BehavioralFeature uml2withid_behavioralfeature) {
        this.uml2withid_behavioralfeature = uml2withid_behavioralfeature;
    }
    public UML2WithID_Connector getUml2withid_connector() {
        return uml2withid_connector;
    }

    public void setUml2withid_connector(UML2WithID_Connector uml2withid_connector) {
        this.uml2withid_connector = uml2withid_connector;
    }
    public UML2WithID_BehavioralFeature getUml2withid_behavioralfeature() {
        return uml2withid_behavioralfeature;
    }

    public void setUml2withid_behavioralfeature(UML2WithID_BehavioralFeature uml2withid_behavioralfeature) {
        this.uml2withid_behavioralfeature = uml2withid_behavioralfeature;
    }
    public UML2WithID_BehavioredClassifier getUml2withid_behavioredclassifier() {
        return uml2withid_behavioredclassifier;
    }

    public void setUml2withid_behavioredclassifier(UML2WithID_BehavioredClassifier uml2withid_behavioredclassifier) {
        this.uml2withid_behavioredclassifier = uml2withid_behavioredclassifier;
    }
    public UML2WithID_BehavioredClassifier getUml2withid_behavioredclassifier() {
        return uml2withid_behavioredclassifier;
    }

    public void setUml2withid_behavioredclassifier(UML2WithID_BehavioredClassifier uml2withid_behavioredclassifier) {
        this.uml2withid_behavioredclassifier = uml2withid_behavioredclassifier;
    }
    public List<UML2WithID_ParameterSet> getUml2withid_parametersets() {
        return uml2withid_parametersets;
    }

    public void addUml2withid_parameterset(Uml2withid_parameterset uml2withid_parameterset) {
        this.uml2withid_parametersets.add(uml2withid_parameterset);
    }
    public UML2WithID_Behavior getUml2withid_behavior() {
        return uml2withid_behavior;
    }

    public void setUml2withid_behavior(UML2WithID_Behavior uml2withid_behavior) {
        this.uml2withid_behavior = uml2withid_behavior;
    }
    public UML2WithID_BehavioredClassifier getUml2withid_behavioredclassifier() {
        return uml2withid_behavioredclassifier;
    }

    public void setUml2withid_behavioredclassifier(UML2WithID_BehavioredClassifier uml2withid_behavioredclassifier) {
        this.uml2withid_behavioredclassifier = uml2withid_behavioredclassifier;
    }

}
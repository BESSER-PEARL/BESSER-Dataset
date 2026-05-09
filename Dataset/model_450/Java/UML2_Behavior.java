





import java.util.List;
import java.util.ArrayList;

public class UML2_Behavior extends Class {

    private boolean isReentrant;





    private List<UML2_ParameterSet> uml2_parametersets;




    private UML2_BehavioredClassifier uml2_behavioredclassifier;




    private UML2_Connector uml2_connector;




    private UML2_BehavioralFeature uml2_behavioralfeature;




    private List<UML2_Constraint> uml2_constraints;




    private List<UML2_Behavior> uml2_behaviors;




    private UML2_BehavioredClassifier uml2_behavioredclassifier;




    private UML2_BehavioralFeature uml2_behavioralfeature;




    private List<UML2_Constraint> uml2_constraints;




    private List<UML2_Parameter> uml2_parameters;




    private List<UML2_Parameter> uml2_parameters;




    private UML2_BehavioredClassifier uml2_behavioredclassifier;




    private List<UML2_Parameter> uml2_parameters;


    public UML2_Behavior(
        boolean isReentrant    ) {
        super(
        );
        this.isReentrant = isReentrant;
        this.uml2_parametersets = new ArrayList<>();
        this.uml2_constraints = new ArrayList<>();
        this.uml2_behaviors = new ArrayList<>();
        this.uml2_constraints = new ArrayList<>();
        this.uml2_parameters = new ArrayList<>();
        this.uml2_parameters = new ArrayList<>();
        this.uml2_parameters = new ArrayList<>();
    }

    public UML2_Behavior(
        boolean isReentrant        ArrayList<UML2_ParameterSet> uml2_parametersets,        ArrayList<UML2_Constraint> uml2_constraints,        ArrayList<UML2_Behavior> uml2_behaviors,        ArrayList<UML2_Constraint> uml2_constraints,        ArrayList<UML2_Parameter> uml2_parameters,        ArrayList<UML2_Parameter> uml2_parameters,        ArrayList<UML2_Parameter> uml2_parameters    ) {
        this.isReentrant = isReentrant;
        this.uml2_parametersets = uml2_parametersets;
        this.uml2_constraints = uml2_constraints;
        this.uml2_behaviors = uml2_behaviors;
        this.uml2_constraints = uml2_constraints;
        this.uml2_parameters = uml2_parameters;
        this.uml2_parameters = uml2_parameters;
        this.uml2_parameters = uml2_parameters;
    }

    public boolean getIsreentrant() {
        return isReentrant;
    }

    public void setIsreentrant(boolean isReentrant) {
        this.isReentrant = isReentrant;
    }

    public List<UML2_ParameterSet> getUml2_parametersets() {
        return uml2_parametersets;
    }

    public void addUml2_parameterset(Uml2_parameterset uml2_parameterset) {
        this.uml2_parametersets.add(uml2_parameterset);
    }
    public UML2_BehavioredClassifier getUml2_behavioredclassifier() {
        return uml2_behavioredclassifier;
    }

    public void setUml2_behavioredclassifier(UML2_BehavioredClassifier uml2_behavioredclassifier) {
        this.uml2_behavioredclassifier = uml2_behavioredclassifier;
    }
    public UML2_Connector getUml2_connector() {
        return uml2_connector;
    }

    public void setUml2_connector(UML2_Connector uml2_connector) {
        this.uml2_connector = uml2_connector;
    }
    public UML2_BehavioralFeature getUml2_behavioralfeature() {
        return uml2_behavioralfeature;
    }

    public void setUml2_behavioralfeature(UML2_BehavioralFeature uml2_behavioralfeature) {
        this.uml2_behavioralfeature = uml2_behavioralfeature;
    }
    public List<UML2_Constraint> getUml2_constraints() {
        return uml2_constraints;
    }

    public void addUml2_constraint(Uml2_constraint uml2_constraint) {
        this.uml2_constraints.add(uml2_constraint);
    }
    public List<UML2_Behavior> getUml2_behaviors() {
        return uml2_behaviors;
    }

    public void addUml2_behavior(Uml2_behavior uml2_behavior) {
        this.uml2_behaviors.add(uml2_behavior);
    }
    public UML2_BehavioredClassifier getUml2_behavioredclassifier() {
        return uml2_behavioredclassifier;
    }

    public void setUml2_behavioredclassifier(UML2_BehavioredClassifier uml2_behavioredclassifier) {
        this.uml2_behavioredclassifier = uml2_behavioredclassifier;
    }
    public UML2_BehavioralFeature getUml2_behavioralfeature() {
        return uml2_behavioralfeature;
    }

    public void setUml2_behavioralfeature(UML2_BehavioralFeature uml2_behavioralfeature) {
        this.uml2_behavioralfeature = uml2_behavioralfeature;
    }
    public List<UML2_Constraint> getUml2_constraints() {
        return uml2_constraints;
    }

    public void addUml2_constraint(Uml2_constraint uml2_constraint) {
        this.uml2_constraints.add(uml2_constraint);
    }
    public List<UML2_Parameter> getUml2_parameters() {
        return uml2_parameters;
    }

    public void addUml2_parameter(Uml2_parameter uml2_parameter) {
        this.uml2_parameters.add(uml2_parameter);
    }
    public List<UML2_Parameter> getUml2_parameters() {
        return uml2_parameters;
    }

    public void addUml2_parameter(Uml2_parameter uml2_parameter) {
        this.uml2_parameters.add(uml2_parameter);
    }
    public UML2_BehavioredClassifier getUml2_behavioredclassifier() {
        return uml2_behavioredclassifier;
    }

    public void setUml2_behavioredclassifier(UML2_BehavioredClassifier uml2_behavioredclassifier) {
        this.uml2_behavioredclassifier = uml2_behavioredclassifier;
    }
    public List<UML2_Parameter> getUml2_parameters() {
        return uml2_parameters;
    }

    public void addUml2_parameter(Uml2_parameter uml2_parameter) {
        this.uml2_parameters.add(uml2_parameter);
    }

}
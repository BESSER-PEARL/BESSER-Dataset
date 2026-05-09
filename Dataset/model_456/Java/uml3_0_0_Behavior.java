





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_Behavior extends Class {

    private String isReentrant;





    private List<uml3_0_0_Behavior> uml3_0_0_behaviors;




    private List<uml3_0_0_Parameter> uml3_0_0_parameters;




    private List<uml3_0_0_Constraint> uml3_0_0_constraints;




    private uml3_0_0_Transition uml3_0_0_transition;




    private uml3_0_0_State uml3_0_0_state;




    private uml3_0_0_State uml3_0_0_state;




    private uml3_0_0_State uml3_0_0_state;




    private uml3_0_0_BehavioredClassifier uml3_0_0_behavioredclassifier;




    private uml3_0_0_ObjectNode uml3_0_0_objectnode;




    private uml3_0_0_BehavioredClassifier uml3_0_0_behavioredclassifier;




    private uml3_0_0_BehavioredClassifier uml3_0_0_behavioredclassifier;




    private uml3_0_0_BehavioralFeature uml3_0_0_behavioralfeature;




    private List<uml3_0_0_ParameterSet> uml3_0_0_parametersets;




    private uml3_0_0_BehavioralFeature uml3_0_0_behavioralfeature;




    private List<uml3_0_0_Constraint> uml3_0_0_constraints;


    public uml3_0_0_Behavior(
        String isReentrant    ) {
        super(
        );
        this.isReentrant = isReentrant;
        this.uml3_0_0_behaviors = new ArrayList<>();
        this.uml3_0_0_parameters = new ArrayList<>();
        this.uml3_0_0_constraints = new ArrayList<>();
        this.uml3_0_0_parametersets = new ArrayList<>();
        this.uml3_0_0_constraints = new ArrayList<>();
    }

    public uml3_0_0_Behavior(
        String isReentrant        ArrayList<uml3_0_0_Behavior> uml3_0_0_behaviors,        ArrayList<uml3_0_0_Parameter> uml3_0_0_parameters,        ArrayList<uml3_0_0_Constraint> uml3_0_0_constraints,        ArrayList<uml3_0_0_ParameterSet> uml3_0_0_parametersets,        ArrayList<uml3_0_0_Constraint> uml3_0_0_constraints    ) {
        this.isReentrant = isReentrant;
        this.uml3_0_0_behaviors = uml3_0_0_behaviors;
        this.uml3_0_0_parameters = uml3_0_0_parameters;
        this.uml3_0_0_constraints = uml3_0_0_constraints;
        this.uml3_0_0_parametersets = uml3_0_0_parametersets;
        this.uml3_0_0_constraints = uml3_0_0_constraints;
    }

    public String getIsreentrant() {
        return isReentrant;
    }

    public void setIsreentrant(String isReentrant) {
        this.isReentrant = isReentrant;
    }

    public List<uml3_0_0_Behavior> getUml3_0_0_behaviors() {
        return uml3_0_0_behaviors;
    }

    public void addUml3_0_0_behavior(Uml3_0_0_behavior uml3_0_0_behavior) {
        this.uml3_0_0_behaviors.add(uml3_0_0_behavior);
    }
    public List<uml3_0_0_Parameter> getUml3_0_0_parameters() {
        return uml3_0_0_parameters;
    }

    public void addUml3_0_0_parameter(Uml3_0_0_parameter uml3_0_0_parameter) {
        this.uml3_0_0_parameters.add(uml3_0_0_parameter);
    }
    public List<uml3_0_0_Constraint> getUml3_0_0_constraints() {
        return uml3_0_0_constraints;
    }

    public void addUml3_0_0_constraint(Uml3_0_0_constraint uml3_0_0_constraint) {
        this.uml3_0_0_constraints.add(uml3_0_0_constraint);
    }
    public uml3_0_0_Transition getUml3_0_0_transition() {
        return uml3_0_0_transition;
    }

    public void setUml3_0_0_transition(uml3_0_0_Transition uml3_0_0_transition) {
        this.uml3_0_0_transition = uml3_0_0_transition;
    }
    public uml3_0_0_State getUml3_0_0_state() {
        return uml3_0_0_state;
    }

    public void setUml3_0_0_state(uml3_0_0_State uml3_0_0_state) {
        this.uml3_0_0_state = uml3_0_0_state;
    }
    public uml3_0_0_State getUml3_0_0_state() {
        return uml3_0_0_state;
    }

    public void setUml3_0_0_state(uml3_0_0_State uml3_0_0_state) {
        this.uml3_0_0_state = uml3_0_0_state;
    }
    public uml3_0_0_State getUml3_0_0_state() {
        return uml3_0_0_state;
    }

    public void setUml3_0_0_state(uml3_0_0_State uml3_0_0_state) {
        this.uml3_0_0_state = uml3_0_0_state;
    }
    public uml3_0_0_BehavioredClassifier getUml3_0_0_behavioredclassifier() {
        return uml3_0_0_behavioredclassifier;
    }

    public void setUml3_0_0_behavioredclassifier(uml3_0_0_BehavioredClassifier uml3_0_0_behavioredclassifier) {
        this.uml3_0_0_behavioredclassifier = uml3_0_0_behavioredclassifier;
    }
    public uml3_0_0_ObjectNode getUml3_0_0_objectnode() {
        return uml3_0_0_objectnode;
    }

    public void setUml3_0_0_objectnode(uml3_0_0_ObjectNode uml3_0_0_objectnode) {
        this.uml3_0_0_objectnode = uml3_0_0_objectnode;
    }
    public uml3_0_0_BehavioredClassifier getUml3_0_0_behavioredclassifier() {
        return uml3_0_0_behavioredclassifier;
    }

    public void setUml3_0_0_behavioredclassifier(uml3_0_0_BehavioredClassifier uml3_0_0_behavioredclassifier) {
        this.uml3_0_0_behavioredclassifier = uml3_0_0_behavioredclassifier;
    }
    public uml3_0_0_BehavioredClassifier getUml3_0_0_behavioredclassifier() {
        return uml3_0_0_behavioredclassifier;
    }

    public void setUml3_0_0_behavioredclassifier(uml3_0_0_BehavioredClassifier uml3_0_0_behavioredclassifier) {
        this.uml3_0_0_behavioredclassifier = uml3_0_0_behavioredclassifier;
    }
    public uml3_0_0_BehavioralFeature getUml3_0_0_behavioralfeature() {
        return uml3_0_0_behavioralfeature;
    }

    public void setUml3_0_0_behavioralfeature(uml3_0_0_BehavioralFeature uml3_0_0_behavioralfeature) {
        this.uml3_0_0_behavioralfeature = uml3_0_0_behavioralfeature;
    }
    public List<uml3_0_0_ParameterSet> getUml3_0_0_parametersets() {
        return uml3_0_0_parametersets;
    }

    public void addUml3_0_0_parameterset(Uml3_0_0_parameterset uml3_0_0_parameterset) {
        this.uml3_0_0_parametersets.add(uml3_0_0_parameterset);
    }
    public uml3_0_0_BehavioralFeature getUml3_0_0_behavioralfeature() {
        return uml3_0_0_behavioralfeature;
    }

    public void setUml3_0_0_behavioralfeature(uml3_0_0_BehavioralFeature uml3_0_0_behavioralfeature) {
        this.uml3_0_0_behavioralfeature = uml3_0_0_behavioralfeature;
    }
    public List<uml3_0_0_Constraint> getUml3_0_0_constraints() {
        return uml3_0_0_constraints;
    }

    public void addUml3_0_0_constraint(Uml3_0_0_constraint uml3_0_0_constraint) {
        this.uml3_0_0_constraints.add(uml3_0_0_constraint);
    }

}






import java.util.List;
import java.util.ArrayList;

public class uml_Behavior extends Class {

    private String isReentrant;





    private List<uml_Constraint> uml_constraints;




    private uml_State uml_state;




    private List<uml_Parameter> uml_parameters;




    private uml_State uml_state;




    private uml_Behavior uml_behavior;




    private List<uml_ParameterSet> uml_parametersets;




    private uml_BehavioralFeature uml_behavioralfeature;




    private uml_OpaqueExpression uml_opaqueexpression;




    private uml_ObjectNode uml_objectnode;




    private uml_BehavioredClassifier uml_behavioredclassifier;




    private uml_BehavioredClassifier uml_behavioredclassifier;




    private List<uml_Constraint> uml_constraints;




    private uml_BehavioredClassifier uml_behavioredclassifier;




    private uml_Transition uml_transition;




    private uml_State uml_state;




    private uml_BehavioralFeature uml_behavioralfeature;


    public uml_Behavior(
        String isReentrant    ) {
        super(
        );
        this.isReentrant = isReentrant;
        this.uml_constraints = new ArrayList<>();
        this.uml_parameters = new ArrayList<>();
        this.uml_parametersets = new ArrayList<>();
        this.uml_constraints = new ArrayList<>();
    }

    public uml_Behavior(
        String isReentrant        ArrayList<uml_Constraint> uml_constraints,        ArrayList<uml_Parameter> uml_parameters,        ArrayList<uml_ParameterSet> uml_parametersets,        ArrayList<uml_Constraint> uml_constraints    ) {
        this.isReentrant = isReentrant;
        this.uml_constraints = uml_constraints;
        this.uml_parameters = uml_parameters;
        this.uml_parametersets = uml_parametersets;
        this.uml_constraints = uml_constraints;
    }

    public String getIsreentrant() {
        return isReentrant;
    }

    public void setIsreentrant(String isReentrant) {
        this.isReentrant = isReentrant;
    }

    public List<uml_Constraint> getUml_constraints() {
        return uml_constraints;
    }

    public void addUml_constraint(Uml_constraint uml_constraint) {
        this.uml_constraints.add(uml_constraint);
    }
    public uml_State getUml_state() {
        return uml_state;
    }

    public void setUml_state(uml_State uml_state) {
        this.uml_state = uml_state;
    }
    public List<uml_Parameter> getUml_parameters() {
        return uml_parameters;
    }

    public void addUml_parameter(Uml_parameter uml_parameter) {
        this.uml_parameters.add(uml_parameter);
    }
    public uml_State getUml_state() {
        return uml_state;
    }

    public void setUml_state(uml_State uml_state) {
        this.uml_state = uml_state;
    }
    public uml_Behavior getUml_behavior() {
        return uml_behavior;
    }

    public void setUml_behavior(uml_Behavior uml_behavior) {
        this.uml_behavior = uml_behavior;
    }
    public List<uml_ParameterSet> getUml_parametersets() {
        return uml_parametersets;
    }

    public void addUml_parameterset(Uml_parameterset uml_parameterset) {
        this.uml_parametersets.add(uml_parameterset);
    }
    public uml_BehavioralFeature getUml_behavioralfeature() {
        return uml_behavioralfeature;
    }

    public void setUml_behavioralfeature(uml_BehavioralFeature uml_behavioralfeature) {
        this.uml_behavioralfeature = uml_behavioralfeature;
    }
    public uml_OpaqueExpression getUml_opaqueexpression() {
        return uml_opaqueexpression;
    }

    public void setUml_opaqueexpression(uml_OpaqueExpression uml_opaqueexpression) {
        this.uml_opaqueexpression = uml_opaqueexpression;
    }
    public uml_ObjectNode getUml_objectnode() {
        return uml_objectnode;
    }

    public void setUml_objectnode(uml_ObjectNode uml_objectnode) {
        this.uml_objectnode = uml_objectnode;
    }
    public uml_BehavioredClassifier getUml_behavioredclassifier() {
        return uml_behavioredclassifier;
    }

    public void setUml_behavioredclassifier(uml_BehavioredClassifier uml_behavioredclassifier) {
        this.uml_behavioredclassifier = uml_behavioredclassifier;
    }
    public uml_BehavioredClassifier getUml_behavioredclassifier() {
        return uml_behavioredclassifier;
    }

    public void setUml_behavioredclassifier(uml_BehavioredClassifier uml_behavioredclassifier) {
        this.uml_behavioredclassifier = uml_behavioredclassifier;
    }
    public List<uml_Constraint> getUml_constraints() {
        return uml_constraints;
    }

    public void addUml_constraint(Uml_constraint uml_constraint) {
        this.uml_constraints.add(uml_constraint);
    }
    public uml_BehavioredClassifier getUml_behavioredclassifier() {
        return uml_behavioredclassifier;
    }

    public void setUml_behavioredclassifier(uml_BehavioredClassifier uml_behavioredclassifier) {
        this.uml_behavioredclassifier = uml_behavioredclassifier;
    }
    public uml_Transition getUml_transition() {
        return uml_transition;
    }

    public void setUml_transition(uml_Transition uml_transition) {
        this.uml_transition = uml_transition;
    }
    public uml_State getUml_state() {
        return uml_state;
    }

    public void setUml_state(uml_State uml_state) {
        this.uml_state = uml_state;
    }
    public uml_BehavioralFeature getUml_behavioralfeature() {
        return uml_behavioralfeature;
    }

    public void setUml_behavioralfeature(uml_BehavioralFeature uml_behavioralfeature) {
        this.uml_behavioralfeature = uml_behavioralfeature;
    }

}
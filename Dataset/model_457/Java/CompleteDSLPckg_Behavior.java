





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_Behavior extends Class {

    private boolean isReentrant;





    private CompleteDSLPckg_State completedslpckg_state;




    private CompleteDSLPckg_BehavioralFeature completedslpckg_behavioralfeature;




    private List<CompleteDSLPckg_Constraint> completedslpckg_constraints;




    private CompleteDSLPckg_Transition completedslpckg_transition;




    private CompleteDSLPckg_OpaqueExpression completedslpckg_opaqueexpression;




    private CompleteDSLPckg_State completedslpckg_state;




    private CompleteDSLPckg_State completedslpckg_state;




    private CompleteDSLPckg_Behavior completedslpckg_behavior;




    private List<CompleteDSLPckg_Constraint> completedslpckg_constraints;




    private List<CompleteDSLPckg_Parameter> completedslpckg_parameters;


    public CompleteDSLPckg_Behavior(
        boolean isReentrant    ) {
        super(
        );
        this.isReentrant = isReentrant;
        this.completedslpckg_constraints = new ArrayList<>();
        this.completedslpckg_constraints = new ArrayList<>();
        this.completedslpckg_parameters = new ArrayList<>();
    }

    public CompleteDSLPckg_Behavior(
        boolean isReentrant        ArrayList<CompleteDSLPckg_Constraint> completedslpckg_constraints,        ArrayList<CompleteDSLPckg_Constraint> completedslpckg_constraints,        ArrayList<CompleteDSLPckg_Parameter> completedslpckg_parameters    ) {
        this.isReentrant = isReentrant;
        this.completedslpckg_constraints = completedslpckg_constraints;
        this.completedslpckg_constraints = completedslpckg_constraints;
        this.completedslpckg_parameters = completedslpckg_parameters;
    }

    public boolean getIsreentrant() {
        return isReentrant;
    }

    public void setIsreentrant(boolean isReentrant) {
        this.isReentrant = isReentrant;
    }

    public CompleteDSLPckg_State getCompletedslpckg_state() {
        return completedslpckg_state;
    }

    public void setCompletedslpckg_state(CompleteDSLPckg_State completedslpckg_state) {
        this.completedslpckg_state = completedslpckg_state;
    }
    public CompleteDSLPckg_BehavioralFeature getCompletedslpckg_behavioralfeature() {
        return completedslpckg_behavioralfeature;
    }

    public void setCompletedslpckg_behavioralfeature(CompleteDSLPckg_BehavioralFeature completedslpckg_behavioralfeature) {
        this.completedslpckg_behavioralfeature = completedslpckg_behavioralfeature;
    }
    public List<CompleteDSLPckg_Constraint> getCompletedslpckg_constraints() {
        return completedslpckg_constraints;
    }

    public void addCompletedslpckg_constraint(Completedslpckg_constraint completedslpckg_constraint) {
        this.completedslpckg_constraints.add(completedslpckg_constraint);
    }
    public CompleteDSLPckg_Transition getCompletedslpckg_transition() {
        return completedslpckg_transition;
    }

    public void setCompletedslpckg_transition(CompleteDSLPckg_Transition completedslpckg_transition) {
        this.completedslpckg_transition = completedslpckg_transition;
    }
    public CompleteDSLPckg_OpaqueExpression getCompletedslpckg_opaqueexpression() {
        return completedslpckg_opaqueexpression;
    }

    public void setCompletedslpckg_opaqueexpression(CompleteDSLPckg_OpaqueExpression completedslpckg_opaqueexpression) {
        this.completedslpckg_opaqueexpression = completedslpckg_opaqueexpression;
    }
    public CompleteDSLPckg_State getCompletedslpckg_state() {
        return completedslpckg_state;
    }

    public void setCompletedslpckg_state(CompleteDSLPckg_State completedslpckg_state) {
        this.completedslpckg_state = completedslpckg_state;
    }
    public CompleteDSLPckg_State getCompletedslpckg_state() {
        return completedslpckg_state;
    }

    public void setCompletedslpckg_state(CompleteDSLPckg_State completedslpckg_state) {
        this.completedslpckg_state = completedslpckg_state;
    }
    public CompleteDSLPckg_Behavior getCompletedslpckg_behavior() {
        return completedslpckg_behavior;
    }

    public void setCompletedslpckg_behavior(CompleteDSLPckg_Behavior completedslpckg_behavior) {
        this.completedslpckg_behavior = completedslpckg_behavior;
    }
    public List<CompleteDSLPckg_Constraint> getCompletedslpckg_constraints() {
        return completedslpckg_constraints;
    }

    public void addCompletedslpckg_constraint(Completedslpckg_constraint completedslpckg_constraint) {
        this.completedslpckg_constraints.add(completedslpckg_constraint);
    }
    public List<CompleteDSLPckg_Parameter> getCompletedslpckg_parameters() {
        return completedslpckg_parameters;
    }

    public void addCompletedslpckg_parameter(Completedslpckg_parameter completedslpckg_parameter) {
        this.completedslpckg_parameters.add(completedslpckg_parameter);
    }

}
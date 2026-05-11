





import java.util.List;
import java.util.ArrayList;

public class internalsm_State  {

    private String label;





    private List<internalsm_Transition> internalsm_transitions;




    private internalsm_Transition internalsm_transition;




    private List<internalsm_Transition> internalsm_transitions;




    private List<internalsm_EventToken> internalsm_eventtokens;




    private internalsm_StateMachine internalsm_statemachine;




    private internalsm_Event internalsm_event;




    private List<internalsm_TimeConstraint> internalsm_timeconstraints;




    private internalsm_EventToken internalsm_eventtoken;




    private internalsm_Transition internalsm_transition;


    public internalsm_State(
        String label    ) {
        this.label = label;
        this.internalsm_transitions = new ArrayList<>();
        this.internalsm_transitions = new ArrayList<>();
        this.internalsm_eventtokens = new ArrayList<>();
        this.internalsm_timeconstraints = new ArrayList<>();
    }

    public internalsm_State(
        String label        ArrayList<internalsm_Transition> internalsm_transitions,        ArrayList<internalsm_Transition> internalsm_transitions,        ArrayList<internalsm_EventToken> internalsm_eventtokens,        ArrayList<internalsm_TimeConstraint> internalsm_timeconstraints    ) {
        this.label = label;
        this.internalsm_transitions = internalsm_transitions;
        this.internalsm_transitions = internalsm_transitions;
        this.internalsm_eventtokens = internalsm_eventtokens;
        this.internalsm_timeconstraints = internalsm_timeconstraints;
    }

    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public List<internalsm_Transition> getInternalsm_transitions() {
        return internalsm_transitions;
    }

    public void addInternalsm_transition(Internalsm_transition internalsm_transition) {
        this.internalsm_transitions.add(internalsm_transition);
    }
    public internalsm_Transition getInternalsm_transition() {
        return internalsm_transition;
    }

    public void setInternalsm_transition(internalsm_Transition internalsm_transition) {
        this.internalsm_transition = internalsm_transition;
    }
    public List<internalsm_Transition> getInternalsm_transitions() {
        return internalsm_transitions;
    }

    public void addInternalsm_transition(Internalsm_transition internalsm_transition) {
        this.internalsm_transitions.add(internalsm_transition);
    }
    public List<internalsm_EventToken> getInternalsm_eventtokens() {
        return internalsm_eventtokens;
    }

    public void addInternalsm_eventtoken(Internalsm_eventtoken internalsm_eventtoken) {
        this.internalsm_eventtokens.add(internalsm_eventtoken);
    }
    public internalsm_StateMachine getInternalsm_statemachine() {
        return internalsm_statemachine;
    }

    public void setInternalsm_statemachine(internalsm_StateMachine internalsm_statemachine) {
        this.internalsm_statemachine = internalsm_statemachine;
    }
    public internalsm_Event getInternalsm_event() {
        return internalsm_event;
    }

    public void setInternalsm_event(internalsm_Event internalsm_event) {
        this.internalsm_event = internalsm_event;
    }
    public List<internalsm_TimeConstraint> getInternalsm_timeconstraints() {
        return internalsm_timeconstraints;
    }

    public void addInternalsm_timeconstraint(Internalsm_timeconstraint internalsm_timeconstraint) {
        this.internalsm_timeconstraints.add(internalsm_timeconstraint);
    }
    public internalsm_EventToken getInternalsm_eventtoken() {
        return internalsm_eventtoken;
    }

    public void setInternalsm_eventtoken(internalsm_EventToken internalsm_eventtoken) {
        this.internalsm_eventtoken = internalsm_eventtoken;
    }
    public internalsm_Transition getInternalsm_transition() {
        return internalsm_transition;
    }

    public void setInternalsm_transition(internalsm_Transition internalsm_transition) {
        this.internalsm_transition = internalsm_transition;
    }

}
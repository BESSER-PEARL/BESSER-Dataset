





import java.util.List;
import java.util.ArrayList;

public class occi_State  {

    private String final;
    private String initial;





    private List<occi_Transition> occi_transitions;




    private occi_FSM occi_fsm;




    private occi_Transition occi_transition;




    private occi_Transition occi_transition;




    private occi_FSM occi_fsm;


    public occi_State(
        String final,        String initial    ) {
        this.final = final;
        this.initial = initial;
        this.occi_transitions = new ArrayList<>();
    }

    public occi_State(
        String final,        String initial        ArrayList<occi_Transition> occi_transitions    ) {
        this.final = final;
        this.initial = initial;
        this.occi_transitions = occi_transitions;
    }

    public String getFinal() {
        return final;
    }

    public void setFinal(String final) {
        this.final = final;
    }
    public String getInitial() {
        return initial;
    }

    public void setInitial(String initial) {
        this.initial = initial;
    }

    public List<occi_Transition> getOcci_transitions() {
        return occi_transitions;
    }

    public void addOcci_transition(Occi_transition occi_transition) {
        this.occi_transitions.add(occi_transition);
    }
    public occi_FSM getOcci_fsm() {
        return occi_fsm;
    }

    public void setOcci_fsm(occi_FSM occi_fsm) {
        this.occi_fsm = occi_fsm;
    }
    public occi_Transition getOcci_transition() {
        return occi_transition;
    }

    public void setOcci_transition(occi_Transition occi_transition) {
        this.occi_transition = occi_transition;
    }
    public occi_Transition getOcci_transition() {
        return occi_transition;
    }

    public void setOcci_transition(occi_Transition occi_transition) {
        this.occi_transition = occi_transition;
    }
    public occi_FSM getOcci_fsm() {
        return occi_fsm;
    }

    public void setOcci_fsm(occi_FSM occi_fsm) {
        this.occi_fsm = occi_fsm;
    }

}
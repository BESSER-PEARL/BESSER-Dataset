





import java.util.List;
import java.util.ArrayList;

public class stateMachineEditRules_State  {

    private String id;
    private boolean isEnd;
    private boolean isStart;





    private List<stateMachineEditRules_Transition> statemachineeditrules_transitions;




    private stateMachineEditRules_Transition statemachineeditrules_transition;




    private List<stateMachineEditRules_Transition> statemachineeditrules_transitions;




    private stateMachineEditRules_Transition statemachineeditrules_transition;


    public stateMachineEditRules_State(
        String id,        boolean isEnd,        boolean isStart    ) {
        this.id = id;
        this.isEnd = isEnd;
        this.isStart = isStart;
        this.statemachineeditrules_transitions = new ArrayList<>();
        this.statemachineeditrules_transitions = new ArrayList<>();
    }

    public stateMachineEditRules_State(
        String id,        boolean isEnd,        boolean isStart        ArrayList<stateMachineEditRules_Transition> statemachineeditrules_transitions,        ArrayList<stateMachineEditRules_Transition> statemachineeditrules_transitions    ) {
        this.id = id;
        this.isEnd = isEnd;
        this.isStart = isStart;
        this.statemachineeditrules_transitions = statemachineeditrules_transitions;
        this.statemachineeditrules_transitions = statemachineeditrules_transitions;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public boolean getIsend() {
        return isEnd;
    }

    public void setIsend(boolean isEnd) {
        this.isEnd = isEnd;
    }
    public boolean getIsstart() {
        return isStart;
    }

    public void setIsstart(boolean isStart) {
        this.isStart = isStart;
    }

    public List<stateMachineEditRules_Transition> getStatemachineeditrules_transitions() {
        return statemachineeditrules_transitions;
    }

    public void addStatemachineeditrules_transition(Statemachineeditrules_transition statemachineeditrules_transition) {
        this.statemachineeditrules_transitions.add(statemachineeditrules_transition);
    }
    public stateMachineEditRules_Transition getStatemachineeditrules_transition() {
        return statemachineeditrules_transition;
    }

    public void setStatemachineeditrules_transition(stateMachineEditRules_Transition statemachineeditrules_transition) {
        this.statemachineeditrules_transition = statemachineeditrules_transition;
    }
    public List<stateMachineEditRules_Transition> getStatemachineeditrules_transitions() {
        return statemachineeditrules_transitions;
    }

    public void addStatemachineeditrules_transition(Statemachineeditrules_transition statemachineeditrules_transition) {
        this.statemachineeditrules_transitions.add(statemachineeditrules_transition);
    }
    public stateMachineEditRules_Transition getStatemachineeditrules_transition() {
        return statemachineeditrules_transition;
    }

    public void setStatemachineeditrules_transition(stateMachineEditRules_Transition statemachineeditrules_transition) {
        this.statemachineeditrules_transition = statemachineeditrules_transition;
    }

}
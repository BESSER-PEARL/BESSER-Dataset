





import java.util.List;
import java.util.ArrayList;

public class StateMachine_Region  {

    private String name;





    private List<StateMachine_Vertex> statemachine_vertexs;




    private StateMachine_StateMachine statemachine_statemachine;




    private StateMachine_State statemachine_state;




    private List<StateMachine_Transition> statemachine_transitions;


    public StateMachine_Region(
        String name    ) {
        this.name = name;
        this.statemachine_vertexs = new ArrayList<>();
        this.statemachine_transitions = new ArrayList<>();
    }

    public StateMachine_Region(
        String name        ArrayList<StateMachine_Vertex> statemachine_vertexs,        ArrayList<StateMachine_Transition> statemachine_transitions    ) {
        this.name = name;
        this.statemachine_vertexs = statemachine_vertexs;
        this.statemachine_transitions = statemachine_transitions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<StateMachine_Vertex> getStatemachine_vertexs() {
        return statemachine_vertexs;
    }

    public void addStatemachine_vertex(Statemachine_vertex statemachine_vertex) {
        this.statemachine_vertexs.add(statemachine_vertex);
    }
    public StateMachine_StateMachine getStatemachine_statemachine() {
        return statemachine_statemachine;
    }

    public void setStatemachine_statemachine(StateMachine_StateMachine statemachine_statemachine) {
        this.statemachine_statemachine = statemachine_statemachine;
    }
    public StateMachine_State getStatemachine_state() {
        return statemachine_state;
    }

    public void setStatemachine_state(StateMachine_State statemachine_state) {
        this.statemachine_state = statemachine_state;
    }
    public List<StateMachine_Transition> getStatemachine_transitions() {
        return statemachine_transitions;
    }

    public void addStatemachine_transition(Statemachine_transition statemachine_transition) {
        this.statemachine_transitions.add(statemachine_transition);
    }

}
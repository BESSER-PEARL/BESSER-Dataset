





import java.util.List;
import java.util.ArrayList;

public class StateMachineHyperedges_Transition  {

    private String name;





    private StateMachineHyperedges_StateVertex statemachinehyperedges_statevertex;




    private List<StateMachineHyperedges_StateVertex> statemachinehyperedges_statevertexs;




    private StateMachineHyperedges_StateVertex statemachinehyperedges_statevertex;




    private List<StateMachineHyperedges_StateVertex> statemachinehyperedges_statevertexs;




    private StateMachineHyperedges_StateMachine statemachinehyperedges_statemachine;




    private StateMachineHyperedges_Event statemachinehyperedges_event;


    public StateMachineHyperedges_Transition(
        String name    ) {
        this.name = name;
        this.statemachinehyperedges_statevertexs = new ArrayList<>();
        this.statemachinehyperedges_statevertexs = new ArrayList<>();
    }

    public StateMachineHyperedges_Transition(
        String name        ArrayList<StateMachineHyperedges_StateVertex> statemachinehyperedges_statevertexs,        ArrayList<StateMachineHyperedges_StateVertex> statemachinehyperedges_statevertexs    ) {
        this.name = name;
        this.statemachinehyperedges_statevertexs = statemachinehyperedges_statevertexs;
        this.statemachinehyperedges_statevertexs = statemachinehyperedges_statevertexs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public StateMachineHyperedges_StateVertex getStatemachinehyperedges_statevertex() {
        return statemachinehyperedges_statevertex;
    }

    public void setStatemachinehyperedges_statevertex(StateMachineHyperedges_StateVertex statemachinehyperedges_statevertex) {
        this.statemachinehyperedges_statevertex = statemachinehyperedges_statevertex;
    }
    public List<StateMachineHyperedges_StateVertex> getStatemachinehyperedges_statevertexs() {
        return statemachinehyperedges_statevertexs;
    }

    public void addStatemachinehyperedges_statevertex(Statemachinehyperedges_statevertex statemachinehyperedges_statevertex) {
        this.statemachinehyperedges_statevertexs.add(statemachinehyperedges_statevertex);
    }
    public StateMachineHyperedges_StateVertex getStatemachinehyperedges_statevertex() {
        return statemachinehyperedges_statevertex;
    }

    public void setStatemachinehyperedges_statevertex(StateMachineHyperedges_StateVertex statemachinehyperedges_statevertex) {
        this.statemachinehyperedges_statevertex = statemachinehyperedges_statevertex;
    }
    public List<StateMachineHyperedges_StateVertex> getStatemachinehyperedges_statevertexs() {
        return statemachinehyperedges_statevertexs;
    }

    public void addStatemachinehyperedges_statevertex(Statemachinehyperedges_statevertex statemachinehyperedges_statevertex) {
        this.statemachinehyperedges_statevertexs.add(statemachinehyperedges_statevertex);
    }
    public StateMachineHyperedges_StateMachine getStatemachinehyperedges_statemachine() {
        return statemachinehyperedges_statemachine;
    }

    public void setStatemachinehyperedges_statemachine(StateMachineHyperedges_StateMachine statemachinehyperedges_statemachine) {
        this.statemachinehyperedges_statemachine = statemachinehyperedges_statemachine;
    }
    public StateMachineHyperedges_Event getStatemachinehyperedges_event() {
        return statemachinehyperedges_event;
    }

    public void setStatemachinehyperedges_event(StateMachineHyperedges_Event statemachinehyperedges_event) {
        this.statemachinehyperedges_event = statemachinehyperedges_event;
    }

}
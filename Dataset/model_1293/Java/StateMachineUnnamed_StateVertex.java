





import java.util.List;
import java.util.ArrayList;

public class StateMachineUnnamed_StateVertex  {

    private String name;





    private StateMachineUnnamed_StateMachine statemachineunnamed_statemachine;




    private List<StateMachineUnnamed_StateVertex> statemachineunnamed_statevertexs;


    public StateMachineUnnamed_StateVertex(
        String name    ) {
        this.name = name;
        this.statemachineunnamed_statevertexs = new ArrayList<>();
    }

    public StateMachineUnnamed_StateVertex(
        String name        ArrayList<StateMachineUnnamed_StateVertex> statemachineunnamed_statevertexs    ) {
        this.name = name;
        this.statemachineunnamed_statevertexs = statemachineunnamed_statevertexs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public StateMachineUnnamed_StateMachine getStatemachineunnamed_statemachine() {
        return statemachineunnamed_statemachine;
    }

    public void setStatemachineunnamed_statemachine(StateMachineUnnamed_StateMachine statemachineunnamed_statemachine) {
        this.statemachineunnamed_statemachine = statemachineunnamed_statemachine;
    }
    public List<StateMachineUnnamed_StateVertex> getStatemachineunnamed_statevertexs() {
        return statemachineunnamed_statevertexs;
    }

    public void addStatemachineunnamed_statevertex(Statemachineunnamed_statevertex statemachineunnamed_statevertex) {
        this.statemachineunnamed_statevertexs.add(statemachineunnamed_statevertex);
    }

}
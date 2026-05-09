





import java.util.List;
import java.util.ArrayList;

public class StateMachineDiagram_meta_State extends Vertex {

    private String name;





    private List<StateMachineDiagram_meta_StateMachine> statemachinediagram_meta_statemachines;


    public StateMachineDiagram_meta_State(
        String name    ) {
        super(
        );
        this.name = name;
        this.statemachinediagram_meta_statemachines = new ArrayList<>();
    }

    public StateMachineDiagram_meta_State(
        String name        ArrayList<StateMachineDiagram_meta_StateMachine> statemachinediagram_meta_statemachines    ) {
        this.name = name;
        this.statemachinediagram_meta_statemachines = statemachinediagram_meta_statemachines;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<StateMachineDiagram_meta_StateMachine> getStatemachinediagram_meta_statemachines() {
        return statemachinediagram_meta_statemachines;
    }

    public void addStatemachinediagram_meta_statemachine(Statemachinediagram_meta_statemachine statemachinediagram_meta_statemachine) {
        this.statemachinediagram_meta_statemachines.add(statemachinediagram_meta_statemachine);
    }

}
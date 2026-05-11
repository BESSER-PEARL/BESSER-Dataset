





import java.util.List;
import java.util.ArrayList;

public class sm_State  {

    private String name;





    private sm_StateMachine sm_statemachine;




    private sm_StateMachine sm_statemachine;




    private List<sm_StateMachine> sm_statemachines;




    private sm_StateMachine sm_statemachine;


    public sm_State(
        String name    ) {
        this.name = name;
        this.sm_statemachines = new ArrayList<>();
    }

    public sm_State(
        String name        ArrayList<sm_StateMachine> sm_statemachines    ) {
        this.name = name;
        this.sm_statemachines = sm_statemachines;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public sm_StateMachine getSm_statemachine() {
        return sm_statemachine;
    }

    public void setSm_statemachine(sm_StateMachine sm_statemachine) {
        this.sm_statemachine = sm_statemachine;
    }
    public sm_StateMachine getSm_statemachine() {
        return sm_statemachine;
    }

    public void setSm_statemachine(sm_StateMachine sm_statemachine) {
        this.sm_statemachine = sm_statemachine;
    }
    public List<sm_StateMachine> getSm_statemachines() {
        return sm_statemachines;
    }

    public void addSm_statemachine(Sm_statemachine sm_statemachine) {
        this.sm_statemachines.add(sm_statemachine);
    }
    public sm_StateMachine getSm_statemachine() {
        return sm_statemachine;
    }

    public void setSm_statemachine(sm_StateMachine sm_statemachine) {
        this.sm_statemachine = sm_statemachine;
    }

}
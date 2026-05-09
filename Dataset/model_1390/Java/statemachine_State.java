





import java.util.List;
import java.util.ArrayList;

public class statemachine_State  {

    private String name;





    private statemachine_MyFSM statemachine_myfsm;


    public statemachine_State(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public statemachine_MyFSM getStatemachine_myfsm() {
        return statemachine_myfsm;
    }

    public void setStatemachine_myfsm(statemachine_MyFSM statemachine_myfsm) {
        this.statemachine_myfsm = statemachine_myfsm;
    }

}
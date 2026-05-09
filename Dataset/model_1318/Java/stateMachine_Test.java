





import java.util.List;
import java.util.ArrayList;

public class stateMachine_Test  {






    private stateMachine_Event statemachine_event;




    private List<stateMachine_Type> statemachine_types;


    public stateMachine_Test(
    ) {
        this.statemachine_types = new ArrayList<>();
    }

    public stateMachine_Test(
        ArrayList<stateMachine_Type> statemachine_types    ) {
        this.statemachine_types = statemachine_types;
    }


    public stateMachine_Event getStatemachine_event() {
        return statemachine_event;
    }

    public void setStatemachine_event(stateMachine_Event statemachine_event) {
        this.statemachine_event = statemachine_event;
    }
    public List<stateMachine_Type> getStatemachine_types() {
        return statemachine_types;
    }

    public void addStatemachine_type(Statemachine_type statemachine_type) {
        this.statemachine_types.add(statemachine_type);
    }

}
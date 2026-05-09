





import java.util.List;
import java.util.ArrayList;

public class statemachine_Thing  {

    private String name;





    private statemachine_State statemachine_state;




    private statemachine_Guard statemachine_guard;


    public statemachine_Thing(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public statemachine_State getStatemachine_state() {
        return statemachine_state;
    }

    public void setStatemachine_state(statemachine_State statemachine_state) {
        this.statemachine_state = statemachine_state;
    }
    public statemachine_Guard getStatemachine_guard() {
        return statemachine_guard;
    }

    public void setStatemachine_guard(statemachine_Guard statemachine_guard) {
        this.statemachine_guard = statemachine_guard;
    }

}






import java.util.List;
import java.util.ArrayList;

public class statemachine_Resource  {

    private String name;





    private statemachine_State statemachine_state;


    public statemachine_Resource(
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

}
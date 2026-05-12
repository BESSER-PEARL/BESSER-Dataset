





import java.util.List;
import java.util.ArrayList;

public class statemachines_State extends StatemachineOwner, AbstractNode, EventBNamed {

    private boolean active;





    private statemachines_State statemachines_state;


    public statemachines_State(
        boolean active    ) {
        super(
        );
        this.active = active;
    }


    public boolean getActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }

    public statemachines_State getStatemachines_state() {
        return statemachines_state;
    }

    public void setStatemachines_state(statemachines_State statemachines_state) {
        this.statemachines_state = statemachines_state;
    }

}
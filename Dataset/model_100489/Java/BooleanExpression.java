





import java.util.List;
import java.util.ArrayList;

public class BooleanExpression  {






    private State_Machines_ChangeEvent state_machines_changeevent;




    private State_Machines_Guard state_machines_guard;


    public BooleanExpression(
    ) {
    }



    public State_Machines_ChangeEvent getState_machines_changeevent() {
        return state_machines_changeevent;
    }

    public void setState_machines_changeevent(State_Machines_ChangeEvent state_machines_changeevent) {
        this.state_machines_changeevent = state_machines_changeevent;
    }
    public State_Machines_Guard getState_machines_guard() {
        return state_machines_guard;
    }

    public void setState_machines_guard(State_Machines_Guard state_machines_guard) {
        this.state_machines_guard = state_machines_guard;
    }

}
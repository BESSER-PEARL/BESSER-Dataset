





import java.util.List;
import java.util.ArrayList;

public class FSM  {






    private HALL_FSM_InitialState hall_fsm_initialstate;




    private HALL_FSM_NamedState hall_fsm_namedstate;




    private HALL_Component hall_component;


    public FSM(
    ) {
    }



    public HALL_FSM_InitialState getHall_fsm_initialstate() {
        return hall_fsm_initialstate;
    }

    public void setHall_fsm_initialstate(HALL_FSM_InitialState hall_fsm_initialstate) {
        this.hall_fsm_initialstate = hall_fsm_initialstate;
    }
    public HALL_FSM_NamedState getHall_fsm_namedstate() {
        return hall_fsm_namedstate;
    }

    public void setHall_fsm_namedstate(HALL_FSM_NamedState hall_fsm_namedstate) {
        this.hall_fsm_namedstate = hall_fsm_namedstate;
    }
    public HALL_Component getHall_component() {
        return hall_component;
    }

    public void setHall_component(HALL_Component hall_component) {
        this.hall_component = hall_component;
    }

}
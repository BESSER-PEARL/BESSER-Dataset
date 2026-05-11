





import java.util.List;
import java.util.ArrayList;

public class sm_Transition  {

    private String name;





    private sm_StateMachine sm_statemachine;




    private sm_State sm_state;




    private sm_State sm_state;


    public sm_Transition(
        String name    ) {
        this.name = name;
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
    public sm_State getSm_state() {
        return sm_state;
    }

    public void setSm_state(sm_State sm_state) {
        this.sm_state = sm_state;
    }
    public sm_State getSm_state() {
        return sm_state;
    }

    public void setSm_state(sm_State sm_state) {
        this.sm_state = sm_state;
    }

}
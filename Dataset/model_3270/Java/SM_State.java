





import java.util.List;
import java.util.ArrayList;

public class SM_State  {

    private String name;





    private SM_StateMachine sm_statemachine;


    public SM_State(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public SM_StateMachine getSm_statemachine() {
        return sm_statemachine;
    }

    public void setSm_statemachine(SM_StateMachine sm_statemachine) {
        this.sm_statemachine = sm_statemachine;
    }

}
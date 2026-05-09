





import java.util.List;
import java.util.ArrayList;

public class NHSM_State  {

    private String name;





    private NHSM_StateMachine nhsm_statemachine;


    public NHSM_State(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public NHSM_StateMachine getNhsm_statemachine() {
        return nhsm_statemachine;
    }

    public void setNhsm_statemachine(NHSM_StateMachine nhsm_statemachine) {
        this.nhsm_statemachine = nhsm_statemachine;
    }

}






import java.util.List;
import java.util.ArrayList;

public class idm_State  {

    private String name;





    private idm_StateMachine idm_statemachine;


    public idm_State(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public idm_StateMachine getIdm_statemachine() {
        return idm_statemachine;
    }

    public void setIdm_statemachine(idm_StateMachine idm_statemachine) {
        this.idm_statemachine = idm_statemachine;
    }

}
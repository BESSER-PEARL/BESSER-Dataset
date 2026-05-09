





import java.util.List;
import java.util.ArrayList;

public class statemachine_MyFSM  {

    private String name;





    private statemachine_InitialState statemachine_initialstate;


    public statemachine_MyFSM(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public statemachine_InitialState getStatemachine_initialstate() {
        return statemachine_initialstate;
    }

    public void setStatemachine_initialstate(statemachine_InitialState statemachine_initialstate) {
        this.statemachine_initialstate = statemachine_initialstate;
    }

}
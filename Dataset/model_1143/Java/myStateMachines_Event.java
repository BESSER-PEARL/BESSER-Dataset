





import java.util.List;
import java.util.ArrayList;

public class myStateMachines_Event  {

    private String name;





    private myStateMachines_Statemachine mystatemachines_statemachine;


    public myStateMachines_Event(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myStateMachines_Statemachine getMystatemachines_statemachine() {
        return mystatemachines_statemachine;
    }

    public void setMystatemachines_statemachine(myStateMachines_Statemachine mystatemachines_statemachine) {
        this.mystatemachines_statemachine = mystatemachines_statemachine;
    }

}
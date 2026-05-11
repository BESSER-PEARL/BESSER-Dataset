





import java.util.List;
import java.util.ArrayList;

public class tp1_Transition  {

    private String name;





    private tp1_StateMachine tp1_statemachine;


    public tp1_Transition(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public tp1_StateMachine getTp1_statemachine() {
        return tp1_statemachine;
    }

    public void setTp1_statemachine(tp1_StateMachine tp1_statemachine) {
        this.tp1_statemachine = tp1_statemachine;
    }

}
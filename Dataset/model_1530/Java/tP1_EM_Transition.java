





import java.util.List;
import java.util.ArrayList;

public class tP1_EM_Transition  {

    private String name;





    private tP1_EM_StateMachine tp1_em_statemachine;


    public tP1_EM_Transition(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public tP1_EM_StateMachine getTp1_em_statemachine() {
        return tp1_em_statemachine;
    }

    public void setTp1_em_statemachine(tP1_EM_StateMachine tp1_em_statemachine) {
        this.tp1_em_statemachine = tp1_em_statemachine;
    }

}
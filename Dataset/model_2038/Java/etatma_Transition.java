





import java.util.List;
import java.util.ArrayList;

public class etatma_Transition  {

    private String name;





    private etatma_StateMachine etatma_statemachine;


    public etatma_Transition(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public etatma_StateMachine getEtatma_statemachine() {
        return etatma_statemachine;
    }

    public void setEtatma_statemachine(etatma_StateMachine etatma_statemachine) {
        this.etatma_statemachine = etatma_statemachine;
    }

}
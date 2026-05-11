





import java.util.List;
import java.util.ArrayList;

public class stm_Event  {

    private String name;





    private stm_Statemachine stm_statemachine;


    public stm_Event(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public stm_Statemachine getStm_statemachine() {
        return stm_statemachine;
    }

    public void setStm_statemachine(stm_Statemachine stm_statemachine) {
        this.stm_statemachine = stm_statemachine;
    }

}
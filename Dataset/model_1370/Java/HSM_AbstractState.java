





import java.util.List;
import java.util.ArrayList;

public class HSM_AbstractState  {

    private String name;





    private HSM_Transition hsm_transition;




    private HSM_Transition hsm_transition;


    public HSM_AbstractState(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public HSM_Transition getHsm_transition() {
        return hsm_transition;
    }

    public void setHsm_transition(HSM_Transition hsm_transition) {
        this.hsm_transition = hsm_transition;
    }
    public HSM_Transition getHsm_transition() {
        return hsm_transition;
    }

    public void setHsm_transition(HSM_Transition hsm_transition) {
        this.hsm_transition = hsm_transition;
    }

}
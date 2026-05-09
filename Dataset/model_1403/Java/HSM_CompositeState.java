





import java.util.List;
import java.util.ArrayList;

public class HSM_CompositeState extends State {






    private HSM_State hsm_state;


    public HSM_CompositeState(
    ) {
        super(
        );
    }



    public HSM_State getHsm_state() {
        return hsm_state;
    }

    public void setHsm_state(HSM_State hsm_state) {
        this.hsm_state = hsm_state;
    }

}
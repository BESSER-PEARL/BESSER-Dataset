





import java.util.List;
import java.util.ArrayList;

public class OrState  {






    private HSM_Transition hsm_transition;




    private HSM_CompoundState hsm_compoundstate;




    private HSM_DataVar hsm_datavar;


    public OrState(
    ) {
    }



    public HSM_Transition getHsm_transition() {
        return hsm_transition;
    }

    public void setHsm_transition(HSM_Transition hsm_transition) {
        this.hsm_transition = hsm_transition;
    }
    public HSM_CompoundState getHsm_compoundstate() {
        return hsm_compoundstate;
    }

    public void setHsm_compoundstate(HSM_CompoundState hsm_compoundstate) {
        this.hsm_compoundstate = hsm_compoundstate;
    }
    public HSM_DataVar getHsm_datavar() {
        return hsm_datavar;
    }

    public void setHsm_datavar(HSM_DataVar hsm_datavar) {
        this.hsm_datavar = hsm_datavar;
    }

}
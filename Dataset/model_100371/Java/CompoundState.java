





import java.util.List;
import java.util.ArrayList;

public class CompoundState  {






    private HSM_AndState hsm_andstate;




    private HSM_OrState hsm_orstate;


    public CompoundState(
    ) {
    }



    public HSM_AndState getHsm_andstate() {
        return hsm_andstate;
    }

    public void setHsm_andstate(HSM_AndState hsm_andstate) {
        this.hsm_andstate = hsm_andstate;
    }
    public HSM_OrState getHsm_orstate() {
        return hsm_orstate;
    }

    public void setHsm_orstate(HSM_OrState hsm_orstate) {
        this.hsm_orstate = hsm_orstate;
    }

}
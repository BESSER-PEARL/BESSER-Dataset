





import java.util.List;
import java.util.ArrayList;

public class HSM_HSM_CompositeState extends HSM_AbstractState {






    private List<HSM_HSM_AbstractState> hsm_hsm_abstractstates;




    private HSM_HSM_AbstractState hsm_hsm_abstractstate;


    public HSM_HSM_CompositeState(
    ) {
        super(
        );
        this.hsm_hsm_abstractstates = new ArrayList<>();
    }

    public HSM_HSM_CompositeState(
        ArrayList<HSM_HSM_AbstractState> hsm_hsm_abstractstates    ) {
        this.hsm_hsm_abstractstates = hsm_hsm_abstractstates;
    }


    public List<HSM_HSM_AbstractState> getHsm_hsm_abstractstates() {
        return hsm_hsm_abstractstates;
    }

    public void addHsm_hsm_abstractstate(Hsm_hsm_abstractstate hsm_hsm_abstractstate) {
        this.hsm_hsm_abstractstates.add(hsm_hsm_abstractstate);
    }
    public HSM_HSM_AbstractState getHsm_hsm_abstractstate() {
        return hsm_hsm_abstractstate;
    }

    public void setHsm_hsm_abstractstate(HSM_HSM_AbstractState hsm_hsm_abstractstate) {
        this.hsm_hsm_abstractstate = hsm_hsm_abstractstate;
    }

}
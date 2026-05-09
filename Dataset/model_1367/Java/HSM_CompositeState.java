





import java.util.List;
import java.util.ArrayList;

public class HSM_CompositeState extends AbstractState {






    private HSM_AbstractState hsm_abstractstate;




    private List<HSM_AbstractState> hsm_abstractstates;


    public HSM_CompositeState(
    ) {
        super(
        );
        this.hsm_abstractstates = new ArrayList<>();
    }

    public HSM_CompositeState(
        ArrayList<HSM_AbstractState> hsm_abstractstates    ) {
        this.hsm_abstractstates = hsm_abstractstates;
    }


    public HSM_AbstractState getHsm_abstractstate() {
        return hsm_abstractstate;
    }

    public void setHsm_abstractstate(HSM_AbstractState hsm_abstractstate) {
        this.hsm_abstractstate = hsm_abstractstate;
    }
    public List<HSM_AbstractState> getHsm_abstractstates() {
        return hsm_abstractstates;
    }

    public void addHsm_abstractstate(Hsm_abstractstate hsm_abstractstate) {
        this.hsm_abstractstates.add(hsm_abstractstate);
    }

}
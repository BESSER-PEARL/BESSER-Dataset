





import java.util.List;
import java.util.ArrayList;

public class hsm_CompositeState extends AbstractState {






    private hsm_AbstractState hsm_abstractstate;




    private List<hsm_AbstractState> hsm_abstractstates;


    public hsm_CompositeState(
    ) {
        super(
        );
        this.hsm_abstractstates = new ArrayList<>();
    }

    public hsm_CompositeState(
        ArrayList<hsm_AbstractState> hsm_abstractstates    ) {
        this.hsm_abstractstates = hsm_abstractstates;
    }


    public hsm_AbstractState getHsm_abstractstate() {
        return hsm_abstractstate;
    }

    public void setHsm_abstractstate(hsm_AbstractState hsm_abstractstate) {
        this.hsm_abstractstate = hsm_abstractstate;
    }
    public List<hsm_AbstractState> getHsm_abstractstates() {
        return hsm_abstractstates;
    }

    public void addHsm_abstractstate(Hsm_abstractstate hsm_abstractstate) {
        this.hsm_abstractstates.add(hsm_abstractstate);
    }

}
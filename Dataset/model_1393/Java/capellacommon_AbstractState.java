





import java.util.List;
import java.util.ArrayList;

public class capellacommon_AbstractState extends NamedElement, IState {






    private capellacommon_StateTransition capellacommon_statetransition;




    private capellacommon_Region capellacommon_region;




    private List<capellacommon_AbstractState> capellacommon_abstractstates;




    private capellacommon_StateTransition capellacommon_statetransition;




    private capellacommon_Region capellacommon_region;


    public capellacommon_AbstractState(
    ) {
        super(
        );
        this.capellacommon_abstractstates = new ArrayList<>();
    }

    public capellacommon_AbstractState(
        ArrayList<capellacommon_AbstractState> capellacommon_abstractstates    ) {
        this.capellacommon_abstractstates = capellacommon_abstractstates;
    }


    public capellacommon_StateTransition getCapellacommon_statetransition() {
        return capellacommon_statetransition;
    }

    public void setCapellacommon_statetransition(capellacommon_StateTransition capellacommon_statetransition) {
        this.capellacommon_statetransition = capellacommon_statetransition;
    }
    public capellacommon_Region getCapellacommon_region() {
        return capellacommon_region;
    }

    public void setCapellacommon_region(capellacommon_Region capellacommon_region) {
        this.capellacommon_region = capellacommon_region;
    }
    public List<capellacommon_AbstractState> getCapellacommon_abstractstates() {
        return capellacommon_abstractstates;
    }

    public void addCapellacommon_abstractstate(Capellacommon_abstractstate capellacommon_abstractstate) {
        this.capellacommon_abstractstates.add(capellacommon_abstractstate);
    }
    public capellacommon_StateTransition getCapellacommon_statetransition() {
        return capellacommon_statetransition;
    }

    public void setCapellacommon_statetransition(capellacommon_StateTransition capellacommon_statetransition) {
        this.capellacommon_statetransition = capellacommon_statetransition;
    }
    public capellacommon_Region getCapellacommon_region() {
        return capellacommon_region;
    }

    public void setCapellacommon_region(capellacommon_Region capellacommon_region) {
        this.capellacommon_region = capellacommon_region;
    }

}
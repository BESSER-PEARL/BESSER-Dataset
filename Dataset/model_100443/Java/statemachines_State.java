





import java.util.List;
import java.util.ArrayList;

public class statemachines_State extends EventBNamed, StatemachineOwner, AbstractNode {

    private boolean active;





    private List<Invariant> invariants;




    private statemachines_State statemachines_state;


    public statemachines_State(
        boolean active    ) {
        super(
        );
        this.active = active;
        this.invariants = new ArrayList<>();
    }

    public statemachines_State(
        boolean active        ArrayList<Invariant> invariants    ) {
        this.active = active;
        this.invariants = invariants;
    }

    public boolean getActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }

    public List<Invariant> getInvariants() {
        return invariants;
    }

    public void addInvariant(Invariant invariant) {
        this.invariants.add(invariant);
    }
    public statemachines_State getStatemachines_state() {
        return statemachines_state;
    }

    public void setStatemachines_state(statemachines_State statemachines_state) {
        this.statemachines_state = statemachines_state;
    }

}
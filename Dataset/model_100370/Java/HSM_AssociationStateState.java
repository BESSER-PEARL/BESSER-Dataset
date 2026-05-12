





import java.util.List;
import java.util.ArrayList;

public class HSM_AssociationStateState  {






    private List<StateBase> statebases;




    private Transition transition;




    private List<StateBase> statebases;


    public HSM_AssociationStateState(
    ) {
        this.statebases = new ArrayList<>();
        this.statebases = new ArrayList<>();
    }

    public HSM_AssociationStateState(
        ArrayList<StateBase> statebases,        ArrayList<StateBase> statebases    ) {
        this.statebases = statebases;
        this.statebases = statebases;
    }


    public List<StateBase> getStatebases() {
        return statebases;
    }

    public void addStatebase(Statebase statebase) {
        this.statebases.add(statebase);
    }
    public Transition getTransition() {
        return transition;
    }

    public void setTransition(Transition transition) {
        this.transition = transition;
    }
    public List<StateBase> getStatebases() {
        return statebases;
    }

    public void addStatebase(Statebase statebase) {
        this.statebases.add(statebase);
    }

}
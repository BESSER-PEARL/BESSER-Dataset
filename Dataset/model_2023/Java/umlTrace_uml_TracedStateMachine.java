





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedStateMachine extends TracedBehavior {






    private List<uml_TracedStateMachine> uml_tracedstatemachines;




    private List<uml_TracedRegion> uml_tracedregions;




    private List<uml_TracedState> uml_tracedstates;




    private List<uml_TracedPseudostate> uml_tracedpseudostates;


    public umlTrace_uml_TracedStateMachine(
    ) {
        super(
        );
        this.uml_tracedstatemachines = new ArrayList<>();
        this.uml_tracedregions = new ArrayList<>();
        this.uml_tracedstates = new ArrayList<>();
        this.uml_tracedpseudostates = new ArrayList<>();
    }

    public umlTrace_uml_TracedStateMachine(
        ArrayList<uml_TracedStateMachine> uml_tracedstatemachines,        ArrayList<uml_TracedRegion> uml_tracedregions,        ArrayList<uml_TracedState> uml_tracedstates,        ArrayList<uml_TracedPseudostate> uml_tracedpseudostates    ) {
        this.uml_tracedstatemachines = uml_tracedstatemachines;
        this.uml_tracedregions = uml_tracedregions;
        this.uml_tracedstates = uml_tracedstates;
        this.uml_tracedpseudostates = uml_tracedpseudostates;
    }


    public List<uml_TracedStateMachine> getUml_tracedstatemachines() {
        return uml_tracedstatemachines;
    }

    public void addUml_tracedstatemachine(Uml_tracedstatemachine uml_tracedstatemachine) {
        this.uml_tracedstatemachines.add(uml_tracedstatemachine);
    }
    public List<uml_TracedRegion> getUml_tracedregions() {
        return uml_tracedregions;
    }

    public void addUml_tracedregion(Uml_tracedregion uml_tracedregion) {
        this.uml_tracedregions.add(uml_tracedregion);
    }
    public List<uml_TracedState> getUml_tracedstates() {
        return uml_tracedstates;
    }

    public void addUml_tracedstate(Uml_tracedstate uml_tracedstate) {
        this.uml_tracedstates.add(uml_tracedstate);
    }
    public List<uml_TracedPseudostate> getUml_tracedpseudostates() {
        return uml_tracedpseudostates;
    }

    public void addUml_tracedpseudostate(Uml_tracedpseudostate uml_tracedpseudostate) {
        this.uml_tracedpseudostates.add(uml_tracedpseudostate);
    }

}
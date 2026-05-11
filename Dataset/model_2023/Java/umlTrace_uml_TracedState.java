





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedState extends uml_TracedVertex, uml_TracedRedefinableElement, uml_TracedNamespace {






    private List<uml_TracedTrigger> uml_tracedtriggers;




    private List<uml_TracedRegion> uml_tracedregions;




    private uml_TracedStateMachine uml_tracedstatemachine;




    private uml_TracedConstraint uml_tracedconstraint;




    private uml_TracedState uml_tracedstate;




    private List<uml_TracedPseudostate> uml_tracedpseudostates;




    private List<uml_TracedConnectionPointReference> uml_tracedconnectionpointreferences;


    public umlTrace_uml_TracedState(
    ) {
        super(
        );
        this.uml_tracedtriggers = new ArrayList<>();
        this.uml_tracedregions = new ArrayList<>();
        this.uml_tracedpseudostates = new ArrayList<>();
        this.uml_tracedconnectionpointreferences = new ArrayList<>();
    }

    public umlTrace_uml_TracedState(
        ArrayList<uml_TracedTrigger> uml_tracedtriggers,        ArrayList<uml_TracedRegion> uml_tracedregions,        ArrayList<uml_TracedPseudostate> uml_tracedpseudostates,        ArrayList<uml_TracedConnectionPointReference> uml_tracedconnectionpointreferences    ) {
        this.uml_tracedtriggers = uml_tracedtriggers;
        this.uml_tracedregions = uml_tracedregions;
        this.uml_tracedpseudostates = uml_tracedpseudostates;
        this.uml_tracedconnectionpointreferences = uml_tracedconnectionpointreferences;
    }


    public List<uml_TracedTrigger> getUml_tracedtriggers() {
        return uml_tracedtriggers;
    }

    public void addUml_tracedtrigger(Uml_tracedtrigger uml_tracedtrigger) {
        this.uml_tracedtriggers.add(uml_tracedtrigger);
    }
    public List<uml_TracedRegion> getUml_tracedregions() {
        return uml_tracedregions;
    }

    public void addUml_tracedregion(Uml_tracedregion uml_tracedregion) {
        this.uml_tracedregions.add(uml_tracedregion);
    }
    public uml_TracedStateMachine getUml_tracedstatemachine() {
        return uml_tracedstatemachine;
    }

    public void setUml_tracedstatemachine(uml_TracedStateMachine uml_tracedstatemachine) {
        this.uml_tracedstatemachine = uml_tracedstatemachine;
    }
    public uml_TracedConstraint getUml_tracedconstraint() {
        return uml_tracedconstraint;
    }

    public void setUml_tracedconstraint(uml_TracedConstraint uml_tracedconstraint) {
        this.uml_tracedconstraint = uml_tracedconstraint;
    }
    public uml_TracedState getUml_tracedstate() {
        return uml_tracedstate;
    }

    public void setUml_tracedstate(uml_TracedState uml_tracedstate) {
        this.uml_tracedstate = uml_tracedstate;
    }
    public List<uml_TracedPseudostate> getUml_tracedpseudostates() {
        return uml_tracedpseudostates;
    }

    public void addUml_tracedpseudostate(Uml_tracedpseudostate uml_tracedpseudostate) {
        this.uml_tracedpseudostates.add(uml_tracedpseudostate);
    }
    public List<uml_TracedConnectionPointReference> getUml_tracedconnectionpointreferences() {
        return uml_tracedconnectionpointreferences;
    }

    public void addUml_tracedconnectionpointreference(Uml_tracedconnectionpointreference uml_tracedconnectionpointreference) {
        this.uml_tracedconnectionpointreferences.add(uml_tracedconnectionpointreference);
    }

}
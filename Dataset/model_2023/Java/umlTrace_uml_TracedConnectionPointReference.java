





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedConnectionPointReference extends TracedVertex {






    private List<uml_TracedPseudostate> uml_tracedpseudostates;




    private List<uml_TracedPseudostate> uml_tracedpseudostates;




    private uml_TracedState uml_tracedstate;


    public umlTrace_uml_TracedConnectionPointReference(
    ) {
        super(
        );
        this.uml_tracedpseudostates = new ArrayList<>();
        this.uml_tracedpseudostates = new ArrayList<>();
    }

    public umlTrace_uml_TracedConnectionPointReference(
        ArrayList<uml_TracedPseudostate> uml_tracedpseudostates,        ArrayList<uml_TracedPseudostate> uml_tracedpseudostates    ) {
        this.uml_tracedpseudostates = uml_tracedpseudostates;
        this.uml_tracedpseudostates = uml_tracedpseudostates;
    }


    public List<uml_TracedPseudostate> getUml_tracedpseudostates() {
        return uml_tracedpseudostates;
    }

    public void addUml_tracedpseudostate(Uml_tracedpseudostate uml_tracedpseudostate) {
        this.uml_tracedpseudostates.add(uml_tracedpseudostate);
    }
    public List<uml_TracedPseudostate> getUml_tracedpseudostates() {
        return uml_tracedpseudostates;
    }

    public void addUml_tracedpseudostate(Uml_tracedpseudostate uml_tracedpseudostate) {
        this.uml_tracedpseudostates.add(uml_tracedpseudostate);
    }
    public uml_TracedState getUml_tracedstate() {
        return uml_tracedstate;
    }

    public void setUml_tracedstate(uml_TracedState uml_tracedstate) {
        this.uml_tracedstate = uml_tracedstate;
    }

}
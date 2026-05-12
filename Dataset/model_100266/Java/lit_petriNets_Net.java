





import java.util.List;
import java.util.ArrayList;

public class lit_petriNets_Net  {






    private lit_petriNets_Arc lit_petrinets_arc;




    private List<lit_petriNets_Transition> lit_petrinets_transitions;




    private List<lit_petriNets_Arc> lit_petrinets_arcs;




    private lit_petriNets_Transition lit_petrinets_transition;


    public lit_petriNets_Net(
    ) {
        this.lit_petrinets_transitions = new ArrayList<>();
        this.lit_petrinets_arcs = new ArrayList<>();
    }

    public lit_petriNets_Net(
        ArrayList<lit_petriNets_Transition> lit_petrinets_transitions,        ArrayList<lit_petriNets_Arc> lit_petrinets_arcs    ) {
        this.lit_petrinets_transitions = lit_petrinets_transitions;
        this.lit_petrinets_arcs = lit_petrinets_arcs;
    }


    public lit_petriNets_Arc getLit_petrinets_arc() {
        return lit_petrinets_arc;
    }

    public void setLit_petrinets_arc(lit_petriNets_Arc lit_petrinets_arc) {
        this.lit_petrinets_arc = lit_petrinets_arc;
    }
    public List<lit_petriNets_Transition> getLit_petrinets_transitions() {
        return lit_petrinets_transitions;
    }

    public void addLit_petrinets_transition(Lit_petrinets_transition lit_petrinets_transition) {
        this.lit_petrinets_transitions.add(lit_petrinets_transition);
    }
    public List<lit_petriNets_Arc> getLit_petrinets_arcs() {
        return lit_petrinets_arcs;
    }

    public void addLit_petrinets_arc(Lit_petrinets_arc lit_petrinets_arc) {
        this.lit_petrinets_arcs.add(lit_petrinets_arc);
    }
    public lit_petriNets_Transition getLit_petrinets_transition() {
        return lit_petrinets_transition;
    }

    public void setLit_petrinets_transition(lit_petriNets_Transition lit_petrinets_transition) {
        this.lit_petrinets_transition = lit_petrinets_transition;
    }

}
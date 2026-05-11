





import java.util.List;
import java.util.ArrayList;

public class umlTrace_Values_SemanticVisitor_runtimeModelElement_Value  {






    private Loci_TracedSemanticVisitor loci_tracedsemanticvisitor;




    private List<State> states;


    public umlTrace_Values_SemanticVisitor_runtimeModelElement_Value(
    ) {
        this.states = new ArrayList<>();
    }

    public umlTrace_Values_SemanticVisitor_runtimeModelElement_Value(
        ArrayList<State> states    ) {
        this.states = states;
    }


    public Loci_TracedSemanticVisitor getLoci_tracedsemanticvisitor() {
        return loci_tracedsemanticvisitor;
    }

    public void setLoci_tracedsemanticvisitor(Loci_TracedSemanticVisitor loci_tracedsemanticvisitor) {
        this.loci_tracedsemanticvisitor = loci_tracedsemanticvisitor;
    }
    public List<State> getStates() {
        return states;
    }

    public void addState(State state) {
        this.states.add(state);
    }

}
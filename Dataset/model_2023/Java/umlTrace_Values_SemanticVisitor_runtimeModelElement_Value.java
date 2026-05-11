





import java.util.List;
import java.util.ArrayList;

public class umlTrace_Values_SemanticVisitor_runtimeModelElement_Value  {






    private Loci_TracedSemanticVisitor loci_tracedsemanticvisitor;




    private List<Values_umlTrace_State> values_umltrace_states;




    private uml_TracedElement uml_tracedelement;


    public umlTrace_Values_SemanticVisitor_runtimeModelElement_Value(
    ) {
        this.values_umltrace_states = new ArrayList<>();
    }

    public umlTrace_Values_SemanticVisitor_runtimeModelElement_Value(
        ArrayList<Values_umlTrace_State> values_umltrace_states    ) {
        this.values_umltrace_states = values_umltrace_states;
    }


    public Loci_TracedSemanticVisitor getLoci_tracedsemanticvisitor() {
        return loci_tracedsemanticvisitor;
    }

    public void setLoci_tracedsemanticvisitor(Loci_TracedSemanticVisitor loci_tracedsemanticvisitor) {
        this.loci_tracedsemanticvisitor = loci_tracedsemanticvisitor;
    }
    public List<Values_umlTrace_State> getValues_umltrace_states() {
        return values_umltrace_states;
    }

    public void addValues_umltrace_state(Values_umltrace_state values_umltrace_state) {
        this.values_umltrace_states.add(values_umltrace_state);
    }
    public uml_TracedElement getUml_tracedelement() {
        return uml_tracedelement;
    }

    public void setUml_tracedelement(uml_TracedElement uml_tracedelement) {
        this.uml_tracedelement = uml_tracedelement;
    }

}
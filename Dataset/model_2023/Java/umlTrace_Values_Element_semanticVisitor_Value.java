





import java.util.List;
import java.util.ArrayList;

public class umlTrace_Values_Element_semanticVisitor_Value  {






    private uml_TracedElement uml_tracedelement;




    private List<Values_umlTrace_State> values_umltrace_states;




    private List<Loci_TracedSemanticVisitor> loci_tracedsemanticvisitors;


    public umlTrace_Values_Element_semanticVisitor_Value(
    ) {
        this.values_umltrace_states = new ArrayList<>();
        this.loci_tracedsemanticvisitors = new ArrayList<>();
    }

    public umlTrace_Values_Element_semanticVisitor_Value(
        ArrayList<Values_umlTrace_State> values_umltrace_states,        ArrayList<Loci_TracedSemanticVisitor> loci_tracedsemanticvisitors    ) {
        this.values_umltrace_states = values_umltrace_states;
        this.loci_tracedsemanticvisitors = loci_tracedsemanticvisitors;
    }


    public uml_TracedElement getUml_tracedelement() {
        return uml_tracedelement;
    }

    public void setUml_tracedelement(uml_TracedElement uml_tracedelement) {
        this.uml_tracedelement = uml_tracedelement;
    }
    public List<Values_umlTrace_State> getValues_umltrace_states() {
        return values_umltrace_states;
    }

    public void addValues_umltrace_state(Values_umltrace_state values_umltrace_state) {
        this.values_umltrace_states.add(values_umltrace_state);
    }
    public List<Loci_TracedSemanticVisitor> getLoci_tracedsemanticvisitors() {
        return loci_tracedsemanticvisitors;
    }

    public void addLoci_tracedsemanticvisitor(Loci_tracedsemanticvisitor loci_tracedsemanticvisitor) {
        this.loci_tracedsemanticvisitors.add(loci_tracedsemanticvisitor);
    }

}
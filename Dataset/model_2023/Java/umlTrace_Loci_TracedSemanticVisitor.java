





import java.util.List;
import java.util.ArrayList;

public class umlTrace_Loci_TracedSemanticVisitor  {






    private List<SemanticVisitor_runtimeModelElement_Value> semanticvisitor_runtimemodelelement_values;


    public umlTrace_Loci_TracedSemanticVisitor(
    ) {
        this.semanticvisitor_runtimemodelelement_values = new ArrayList<>();
    }

    public umlTrace_Loci_TracedSemanticVisitor(
        ArrayList<SemanticVisitor_runtimeModelElement_Value> semanticvisitor_runtimemodelelement_values    ) {
        this.semanticvisitor_runtimemodelelement_values = semanticvisitor_runtimemodelelement_values;
    }


    public List<SemanticVisitor_runtimeModelElement_Value> getSemanticvisitor_runtimemodelelement_values() {
        return semanticvisitor_runtimemodelelement_values;
    }

    public void addSemanticvisitor_runtimemodelelement_value(Semanticvisitor_runtimemodelelement_value semanticvisitor_runtimemodelelement_value) {
        this.semanticvisitor_runtimemodelelement_values.add(semanticvisitor_runtimemodelelement_value);
    }

}
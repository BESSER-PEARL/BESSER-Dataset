





import java.util.List;
import java.util.ArrayList;

public class umlTrace_Loci_TracedSemanticVisitor  {






    private List<Values_SemanticVisitor_runtimeModelElement_Value> values_semanticvisitor_runtimemodelelement_values;


    public umlTrace_Loci_TracedSemanticVisitor(
    ) {
        this.values_semanticvisitor_runtimemodelelement_values = new ArrayList<>();
    }

    public umlTrace_Loci_TracedSemanticVisitor(
        ArrayList<Values_SemanticVisitor_runtimeModelElement_Value> values_semanticvisitor_runtimemodelelement_values    ) {
        this.values_semanticvisitor_runtimemodelelement_values = values_semanticvisitor_runtimemodelelement_values;
    }


    public List<Values_SemanticVisitor_runtimeModelElement_Value> getValues_semanticvisitor_runtimemodelelement_values() {
        return values_semanticvisitor_runtimemodelelement_values;
    }

    public void addValues_semanticvisitor_runtimemodelelement_value(Values_semanticvisitor_runtimemodelelement_value values_semanticvisitor_runtimemodelelement_value) {
        this.values_semanticvisitor_runtimemodelelement_values.add(values_semanticvisitor_runtimemodelelement_value);
    }

}






import java.util.List;
import java.util.ArrayList;

public class umlTrace_Kernel_TracedCompoundValue extends TracedStructuredValue {






    private List<CompoundValue_featureValues_Value> compoundvalue_featurevalues_values;


    public umlTrace_Kernel_TracedCompoundValue(
    ) {
        super(
        );
        this.compoundvalue_featurevalues_values = new ArrayList<>();
    }

    public umlTrace_Kernel_TracedCompoundValue(
        ArrayList<CompoundValue_featureValues_Value> compoundvalue_featurevalues_values    ) {
        this.compoundvalue_featurevalues_values = compoundvalue_featurevalues_values;
    }


    public List<CompoundValue_featureValues_Value> getCompoundvalue_featurevalues_values() {
        return compoundvalue_featurevalues_values;
    }

    public void addCompoundvalue_featurevalues_value(Compoundvalue_featurevalues_value compoundvalue_featurevalues_value) {
        this.compoundvalue_featurevalues_values.add(compoundvalue_featurevalues_value);
    }

}
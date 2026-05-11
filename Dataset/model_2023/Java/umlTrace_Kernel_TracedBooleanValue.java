





import java.util.List;
import java.util.ArrayList;

public class umlTrace_Kernel_TracedBooleanValue extends TracedPrimitiveValue {






    private List<BooleanValue_value_BooleanValue_Value> booleanvalue_value_booleanvalue_values;


    public umlTrace_Kernel_TracedBooleanValue(
    ) {
        super(
        );
        this.booleanvalue_value_booleanvalue_values = new ArrayList<>();
    }

    public umlTrace_Kernel_TracedBooleanValue(
        ArrayList<BooleanValue_value_BooleanValue_Value> booleanvalue_value_booleanvalue_values    ) {
        this.booleanvalue_value_booleanvalue_values = booleanvalue_value_booleanvalue_values;
    }


    public List<BooleanValue_value_BooleanValue_Value> getBooleanvalue_value_booleanvalue_values() {
        return booleanvalue_value_booleanvalue_values;
    }

    public void addBooleanvalue_value_booleanvalue_value(Booleanvalue_value_booleanvalue_value booleanvalue_value_booleanvalue_value) {
        this.booleanvalue_value_booleanvalue_values.add(booleanvalue_value_booleanvalue_value);
    }

}
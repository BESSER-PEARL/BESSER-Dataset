





import java.util.List;
import java.util.ArrayList;

public class umlTrace_Kernel_TracedIntegerValue extends TracedPrimitiveValue {






    private List<IntegerValue_value_IntegerValue_Value> integervalue_value_integervalue_values;


    public umlTrace_Kernel_TracedIntegerValue(
    ) {
        super(
        );
        this.integervalue_value_integervalue_values = new ArrayList<>();
    }

    public umlTrace_Kernel_TracedIntegerValue(
        ArrayList<IntegerValue_value_IntegerValue_Value> integervalue_value_integervalue_values    ) {
        this.integervalue_value_integervalue_values = integervalue_value_integervalue_values;
    }


    public List<IntegerValue_value_IntegerValue_Value> getIntegervalue_value_integervalue_values() {
        return integervalue_value_integervalue_values;
    }

    public void addIntegervalue_value_integervalue_value(Integervalue_value_integervalue_value integervalue_value_integervalue_value) {
        this.integervalue_value_integervalue_values.add(integervalue_value_integervalue_value);
    }

}






import java.util.List;
import java.util.ArrayList;

public class umlTrace_Kernel_TracedPrimitiveValue extends TracedValue {






    private List<PrimitiveValue_type_Value> primitivevalue_type_values;


    public umlTrace_Kernel_TracedPrimitiveValue(
    ) {
        super(
        );
        this.primitivevalue_type_values = new ArrayList<>();
    }

    public umlTrace_Kernel_TracedPrimitiveValue(
        ArrayList<PrimitiveValue_type_Value> primitivevalue_type_values    ) {
        this.primitivevalue_type_values = primitivevalue_type_values;
    }


    public List<PrimitiveValue_type_Value> getPrimitivevalue_type_values() {
        return primitivevalue_type_values;
    }

    public void addPrimitivevalue_type_value(Primitivevalue_type_value primitivevalue_type_value) {
        this.primitivevalue_type_values.add(primitivevalue_type_value);
    }

}
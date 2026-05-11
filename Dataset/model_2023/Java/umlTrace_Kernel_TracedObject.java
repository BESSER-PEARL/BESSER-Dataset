





import java.util.List;
import java.util.ArrayList;

public class umlTrace_Kernel_TracedObject extends TracedExtensionalValue {






    private List<Object_types_Value> object_types_values;


    public umlTrace_Kernel_TracedObject(
    ) {
        super(
        );
        this.object_types_values = new ArrayList<>();
    }

    public umlTrace_Kernel_TracedObject(
        ArrayList<Object_types_Value> object_types_values    ) {
        this.object_types_values = object_types_values;
    }


    public List<Object_types_Value> getObject_types_values() {
        return object_types_values;
    }

    public void addObject_types_value(Object_types_value object_types_value) {
        this.object_types_values.add(object_types_value);
    }

}






import java.util.List;
import java.util.ArrayList;

public class umlTrace_Kernel_TracedReference extends TracedStructuredValue {






    private List<Reference_referent_Value> reference_referent_values;


    public umlTrace_Kernel_TracedReference(
    ) {
        super(
        );
        this.reference_referent_values = new ArrayList<>();
    }

    public umlTrace_Kernel_TracedReference(
        ArrayList<Reference_referent_Value> reference_referent_values    ) {
        this.reference_referent_values = reference_referent_values;
    }


    public List<Reference_referent_Value> getReference_referent_values() {
        return reference_referent_values;
    }

    public void addReference_referent_value(Reference_referent_value reference_referent_value) {
        this.reference_referent_values.add(reference_referent_value);
    }

}






import java.util.List;
import java.util.ArrayList;

public class umlTrace_Kernel_TracedExtensionalValue extends TracedCompoundValue {






    private List<ExtensionalValue_locus_ExtensionalValue_Value> extensionalvalue_locus_extensionalvalue_values;


    public umlTrace_Kernel_TracedExtensionalValue(
    ) {
        super(
        );
        this.extensionalvalue_locus_extensionalvalue_values = new ArrayList<>();
    }

    public umlTrace_Kernel_TracedExtensionalValue(
        ArrayList<ExtensionalValue_locus_ExtensionalValue_Value> extensionalvalue_locus_extensionalvalue_values    ) {
        this.extensionalvalue_locus_extensionalvalue_values = extensionalvalue_locus_extensionalvalue_values;
    }


    public List<ExtensionalValue_locus_ExtensionalValue_Value> getExtensionalvalue_locus_extensionalvalue_values() {
        return extensionalvalue_locus_extensionalvalue_values;
    }

    public void addExtensionalvalue_locus_extensionalvalue_value(Extensionalvalue_locus_extensionalvalue_value extensionalvalue_locus_extensionalvalue_value) {
        this.extensionalvalue_locus_extensionalvalue_values.add(extensionalvalue_locus_extensionalvalue_value);
    }

}
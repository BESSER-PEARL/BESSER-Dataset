





import java.util.List;
import java.util.ArrayList;

public class umlTrace_Loci_TracedLocus  {






    private List<Locus_executor_Value> locus_executor_values;




    private List<Locus_factory_Value> locus_factory_values;




    private List<Locus_extensionalValues_Value> locus_extensionalvalues_values;


    public umlTrace_Loci_TracedLocus(
    ) {
        this.locus_executor_values = new ArrayList<>();
        this.locus_factory_values = new ArrayList<>();
        this.locus_extensionalvalues_values = new ArrayList<>();
    }

    public umlTrace_Loci_TracedLocus(
        ArrayList<Locus_executor_Value> locus_executor_values,        ArrayList<Locus_factory_Value> locus_factory_values,        ArrayList<Locus_extensionalValues_Value> locus_extensionalvalues_values    ) {
        this.locus_executor_values = locus_executor_values;
        this.locus_factory_values = locus_factory_values;
        this.locus_extensionalvalues_values = locus_extensionalvalues_values;
    }


    public List<Locus_executor_Value> getLocus_executor_values() {
        return locus_executor_values;
    }

    public void addLocus_executor_value(Locus_executor_value locus_executor_value) {
        this.locus_executor_values.add(locus_executor_value);
    }
    public List<Locus_factory_Value> getLocus_factory_values() {
        return locus_factory_values;
    }

    public void addLocus_factory_value(Locus_factory_value locus_factory_value) {
        this.locus_factory_values.add(locus_factory_value);
    }
    public List<Locus_extensionalValues_Value> getLocus_extensionalvalues_values() {
        return locus_extensionalvalues_values;
    }

    public void addLocus_extensionalvalues_value(Locus_extensionalvalues_value locus_extensionalvalues_value) {
        this.locus_extensionalvalues_values.add(locus_extensionalvalues_value);
    }

}
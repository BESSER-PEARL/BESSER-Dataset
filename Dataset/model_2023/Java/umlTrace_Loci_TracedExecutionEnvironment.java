





import java.util.List;
import java.util.ArrayList;

public class umlTrace_Loci_TracedExecutionEnvironment  {






    private List<ExecutionEnvironment_locus_ExecutionEnvironment_Value> executionenvironment_locus_executionenvironment_values;


    public umlTrace_Loci_TracedExecutionEnvironment(
    ) {
        this.executionenvironment_locus_executionenvironment_values = new ArrayList<>();
    }

    public umlTrace_Loci_TracedExecutionEnvironment(
        ArrayList<ExecutionEnvironment_locus_ExecutionEnvironment_Value> executionenvironment_locus_executionenvironment_values    ) {
        this.executionenvironment_locus_executionenvironment_values = executionenvironment_locus_executionenvironment_values;
    }


    public List<ExecutionEnvironment_locus_ExecutionEnvironment_Value> getExecutionenvironment_locus_executionenvironment_values() {
        return executionenvironment_locus_executionenvironment_values;
    }

    public void addExecutionenvironment_locus_executionenvironment_value(Executionenvironment_locus_executionenvironment_value executionenvironment_locus_executionenvironment_value) {
        this.executionenvironment_locus_executionenvironment_values.add(executionenvironment_locus_executionenvironment_value);
    }

}
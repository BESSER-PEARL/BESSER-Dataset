





import java.util.List;
import java.util.ArrayList;

public class umlTrace_Loci_TracedExecutor  {






    private List<Executor_locus_Executor_Value> executor_locus_executor_values;


    public umlTrace_Loci_TracedExecutor(
    ) {
        this.executor_locus_executor_values = new ArrayList<>();
    }

    public umlTrace_Loci_TracedExecutor(
        ArrayList<Executor_locus_Executor_Value> executor_locus_executor_values    ) {
        this.executor_locus_executor_values = executor_locus_executor_values;
    }


    public List<Executor_locus_Executor_Value> getExecutor_locus_executor_values() {
        return executor_locus_executor_values;
    }

    public void addExecutor_locus_executor_value(Executor_locus_executor_value executor_locus_executor_value) {
        this.executor_locus_executor_values.add(executor_locus_executor_value);
    }

}
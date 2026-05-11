





import java.util.List;
import java.util.ArrayList;

public class umlTrace_Loci_TracedExecutionFactory  {






    private List<ExecutionFactory_locus_ExecutionFactory_Value> executionfactory_locus_executionfactory_values;




    private List<ExecutionFactory_builtInTypes_Value> executionfactory_builtintypes_values;




    private List<ExecutionFactory_primitiveBehaviorPrototypes_Value> executionfactory_primitivebehaviorprototypes_values;


    public umlTrace_Loci_TracedExecutionFactory(
    ) {
        this.executionfactory_locus_executionfactory_values = new ArrayList<>();
        this.executionfactory_builtintypes_values = new ArrayList<>();
        this.executionfactory_primitivebehaviorprototypes_values = new ArrayList<>();
    }

    public umlTrace_Loci_TracedExecutionFactory(
        ArrayList<ExecutionFactory_locus_ExecutionFactory_Value> executionfactory_locus_executionfactory_values,        ArrayList<ExecutionFactory_builtInTypes_Value> executionfactory_builtintypes_values,        ArrayList<ExecutionFactory_primitiveBehaviorPrototypes_Value> executionfactory_primitivebehaviorprototypes_values    ) {
        this.executionfactory_locus_executionfactory_values = executionfactory_locus_executionfactory_values;
        this.executionfactory_builtintypes_values = executionfactory_builtintypes_values;
        this.executionfactory_primitivebehaviorprototypes_values = executionfactory_primitivebehaviorprototypes_values;
    }


    public List<ExecutionFactory_locus_ExecutionFactory_Value> getExecutionfactory_locus_executionfactory_values() {
        return executionfactory_locus_executionfactory_values;
    }

    public void addExecutionfactory_locus_executionfactory_value(Executionfactory_locus_executionfactory_value executionfactory_locus_executionfactory_value) {
        this.executionfactory_locus_executionfactory_values.add(executionfactory_locus_executionfactory_value);
    }
    public List<ExecutionFactory_builtInTypes_Value> getExecutionfactory_builtintypes_values() {
        return executionfactory_builtintypes_values;
    }

    public void addExecutionfactory_builtintypes_value(Executionfactory_builtintypes_value executionfactory_builtintypes_value) {
        this.executionfactory_builtintypes_values.add(executionfactory_builtintypes_value);
    }
    public List<ExecutionFactory_primitiveBehaviorPrototypes_Value> getExecutionfactory_primitivebehaviorprototypes_values() {
        return executionfactory_primitivebehaviorprototypes_values;
    }

    public void addExecutionfactory_primitivebehaviorprototypes_value(Executionfactory_primitivebehaviorprototypes_value executionfactory_primitivebehaviorprototypes_value) {
        this.executionfactory_primitivebehaviorprototypes_values.add(executionfactory_primitivebehaviorprototypes_value);
    }

}
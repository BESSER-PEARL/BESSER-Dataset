





import java.util.List;
import java.util.ArrayList;

public class dsl_ArrayInitializer  {






    private List<dsl_VariableInitializer> dsl_variableinitializers;




    private dsl_VariableInitializer dsl_variableinitializer;


    public dsl_ArrayInitializer(
    ) {
        this.dsl_variableinitializers = new ArrayList<>();
    }

    public dsl_ArrayInitializer(
        ArrayList<dsl_VariableInitializer> dsl_variableinitializers    ) {
        this.dsl_variableinitializers = dsl_variableinitializers;
    }


    public List<dsl_VariableInitializer> getDsl_variableinitializers() {
        return dsl_variableinitializers;
    }

    public void addDsl_variableinitializer(Dsl_variableinitializer dsl_variableinitializer) {
        this.dsl_variableinitializers.add(dsl_variableinitializer);
    }
    public dsl_VariableInitializer getDsl_variableinitializer() {
        return dsl_variableinitializer;
    }

    public void setDsl_variableinitializer(dsl_VariableInitializer dsl_variableinitializer) {
        this.dsl_variableinitializer = dsl_variableinitializer;
    }

}
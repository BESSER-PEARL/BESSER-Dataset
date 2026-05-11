





import java.util.List;
import java.util.ArrayList;

public class Model_AtomicDEVS extends DEVS {






    private List<Model_Variable> model_variables;


    public Model_AtomicDEVS(
    ) {
        super(
        );
        this.model_variables = new ArrayList<>();
    }

    public Model_AtomicDEVS(
        ArrayList<Model_Variable> model_variables    ) {
        this.model_variables = model_variables;
    }


    public List<Model_Variable> getModel_variables() {
        return model_variables;
    }

    public void addModel_variable(Model_variable model_variable) {
        this.model_variables.add(model_variable);
    }

}
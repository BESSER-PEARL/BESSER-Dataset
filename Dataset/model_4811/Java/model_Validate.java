





import java.util.List;
import java.util.ArrayList;

public class model_Validate extends Activity {






    private List<model_Variable> model_variables;


    public model_Validate(
    ) {
        super(
        );
        this.model_variables = new ArrayList<>();
    }

    public model_Validate(
        ArrayList<model_Variable> model_variables    ) {
        this.model_variables = model_variables;
    }


    public List<model_Variable> getModel_variables() {
        return model_variables;
    }

    public void addModel_variable(Model_variable model_variable) {
        this.model_variables.add(model_variable);
    }

}
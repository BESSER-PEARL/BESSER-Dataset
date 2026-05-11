





import java.util.List;
import java.util.ArrayList;

public class asmeta_definitions_DynamicFunction extends BasicFunction {






    private List<FunctionInitialization> functioninitializations;


    public asmeta_definitions_DynamicFunction(
    ) {
        super(
        );
        this.functioninitializations = new ArrayList<>();
    }

    public asmeta_definitions_DynamicFunction(
        ArrayList<FunctionInitialization> functioninitializations    ) {
        this.functioninitializations = functioninitializations;
    }


    public List<FunctionInitialization> getFunctioninitializations() {
        return functioninitializations;
    }

    public void addFunctioninitialization(Functioninitialization functioninitialization) {
        this.functioninitializations.add(functioninitialization);
    }

}
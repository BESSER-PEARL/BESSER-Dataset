





import java.util.List;
import java.util.ArrayList;

public class express_expressions_FunctionCall extends Expression {






    private List<ActualParameter> actualparameters;


    public express_expressions_FunctionCall(
    ) {
        super(
        );
        this.actualparameters = new ArrayList<>();
    }

    public express_expressions_FunctionCall(
        ArrayList<ActualParameter> actualparameters    ) {
        this.actualparameters = actualparameters;
    }


    public List<ActualParameter> getActualparameters() {
        return actualparameters;
    }

    public void addActualparameter(Actualparameter actualparameter) {
        this.actualparameters.add(actualparameter);
    }

}
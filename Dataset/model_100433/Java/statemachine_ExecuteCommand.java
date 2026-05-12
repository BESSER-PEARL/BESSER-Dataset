





import java.util.List;
import java.util.ArrayList;

public class statemachine_ExecuteCommand extends Command {

    private String operation;





    private List<statemachine_Expression> statemachine_expressions;


    public statemachine_ExecuteCommand(
        String operation    ) {
        super(
        );
        this.operation = operation;
        this.statemachine_expressions = new ArrayList<>();
    }

    public statemachine_ExecuteCommand(
        String operation        ArrayList<statemachine_Expression> statemachine_expressions    ) {
        this.operation = operation;
        this.statemachine_expressions = statemachine_expressions;
    }

    public String getOperation() {
        return operation;
    }

    public void setOperation(String operation) {
        this.operation = operation;
    }

    public List<statemachine_Expression> getStatemachine_expressions() {
        return statemachine_expressions;
    }

    public void addStatemachine_expression(Statemachine_expression statemachine_expression) {
        this.statemachine_expressions.add(statemachine_expression);
    }

}
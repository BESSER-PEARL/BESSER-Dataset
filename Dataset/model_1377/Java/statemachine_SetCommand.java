





import java.util.List;
import java.util.ArrayList;

public class statemachine_SetCommand extends Command {

    private String signal;





    private statemachine_Expression statemachine_expression;


    public statemachine_SetCommand(
        String signal    ) {
        super(
        );
        this.signal = signal;
    }


    public String getSignal() {
        return signal;
    }

    public void setSignal(String signal) {
        this.signal = signal;
    }

    public statemachine_Expression getStatemachine_expression() {
        return statemachine_expression;
    }

    public void setStatemachine_expression(statemachine_Expression statemachine_expression) {
        this.statemachine_expression = statemachine_expression;
    }

}
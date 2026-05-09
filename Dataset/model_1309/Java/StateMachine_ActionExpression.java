





import java.util.List;
import java.util.ArrayList;

public class StateMachine_ActionExpression extends Action {

    private String expression;



    public StateMachine_ActionExpression(
        String expression    ) {
        super(
        );
        this.expression = expression;
    }


    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }


}






import java.util.List;
import java.util.ArrayList;

public class simulink_stateflow_Action extends StateflowElement {

    private String expression;



    public simulink_stateflow_Action(
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
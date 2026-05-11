





import java.util.List;
import java.util.ArrayList;

public class fuzzyAutomaton_Output extends Action {

    private String expression;



    public fuzzyAutomaton_Output(
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






import java.util.List;
import java.util.ArrayList;

public class statechart_Guard extends IDBase {

    private String expression;



    public statechart_Guard(
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
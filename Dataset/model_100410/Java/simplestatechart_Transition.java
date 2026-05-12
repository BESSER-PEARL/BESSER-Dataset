





import java.util.List;
import java.util.ArrayList;

public class simplestatechart_Transition extends NamedElement {

    private String expression;



    public simplestatechart_Transition(
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
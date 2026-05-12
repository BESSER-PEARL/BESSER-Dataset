





import java.util.List;
import java.util.ArrayList;

public class simplestatechart101_Transition extends NamedElement {

    private String expression;



    public simplestatechart101_Transition(
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
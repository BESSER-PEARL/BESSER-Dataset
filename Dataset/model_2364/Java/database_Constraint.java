





import java.util.List;
import java.util.ArrayList;

public class database_Constraint extends NamedElement {

    private String expression;



    public database_Constraint(
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






import java.util.List;
import java.util.ArrayList;

public class genericsql_Check extends Constraint {

    private String expression;



    public genericsql_Check(
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
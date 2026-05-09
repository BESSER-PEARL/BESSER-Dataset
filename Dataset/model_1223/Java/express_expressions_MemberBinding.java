





import java.util.List;
import java.util.ArrayList;

public class express_expressions_MemberBinding  {

    private String position;





    private Expression expression;


    public express_expressions_MemberBinding(
        String position    ) {
        this.position = position;
    }


    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }

    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }

}
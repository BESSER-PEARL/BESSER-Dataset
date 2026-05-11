





import java.util.List;
import java.util.ArrayList;

public class frontend_qool_PropertyEqualsPredicate extends MatchPredicate {

    private String propertyName;





    private Expression expression;


    public frontend_qool_PropertyEqualsPredicate(
        String propertyName    ) {
        super(
        );
        this.propertyName = propertyName;
    }


    public String getPropertyname() {
        return propertyName;
    }

    public void setPropertyname(String propertyName) {
        this.propertyName = propertyName;
    }

    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }

}






import java.util.List;
import java.util.ArrayList;

public class cool_DispatchExpression extends PrimaryExpression {






    private List<cool_Expression> cool_expressions;




    private cool_PrimaryExpression cool_primaryexpression;




    private cool_IdentifierRefExpression cool_identifierrefexpression;




    private cool_DispatchExpression cool_dispatchexpression;




    private cool_Type cool_type;


    public cool_DispatchExpression(
    ) {
        super(
        );
        this.cool_expressions = new ArrayList<>();
    }

    public cool_DispatchExpression(
        ArrayList<cool_Expression> cool_expressions    ) {
        this.cool_expressions = cool_expressions;
    }


    public List<cool_Expression> getCool_expressions() {
        return cool_expressions;
    }

    public void addCool_expression(Cool_expression cool_expression) {
        this.cool_expressions.add(cool_expression);
    }
    public cool_PrimaryExpression getCool_primaryexpression() {
        return cool_primaryexpression;
    }

    public void setCool_primaryexpression(cool_PrimaryExpression cool_primaryexpression) {
        this.cool_primaryexpression = cool_primaryexpression;
    }
    public cool_IdentifierRefExpression getCool_identifierrefexpression() {
        return cool_identifierrefexpression;
    }

    public void setCool_identifierrefexpression(cool_IdentifierRefExpression cool_identifierrefexpression) {
        this.cool_identifierrefexpression = cool_identifierrefexpression;
    }
    public cool_DispatchExpression getCool_dispatchexpression() {
        return cool_dispatchexpression;
    }

    public void setCool_dispatchexpression(cool_DispatchExpression cool_dispatchexpression) {
        this.cool_dispatchexpression = cool_dispatchexpression;
    }
    public cool_Type getCool_type() {
        return cool_type;
    }

    public void setCool_type(cool_Type cool_type) {
        this.cool_type = cool_type;
    }

}
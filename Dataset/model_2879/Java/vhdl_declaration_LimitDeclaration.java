





import java.util.List;
import java.util.ArrayList;

public class vhdl_declaration_LimitDeclaration extends type_Typed, MultiNamed, declaration_Declaration {






    private Expression expression;


    public vhdl_declaration_LimitDeclaration(
    ) {
        super(
        );
    }



    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }

}
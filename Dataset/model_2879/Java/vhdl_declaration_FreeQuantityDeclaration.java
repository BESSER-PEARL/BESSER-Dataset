





import java.util.List;
import java.util.ArrayList;

public class vhdl_declaration_FreeQuantityDeclaration extends type_Typed, MultiNamed, declaration_QuantityDeclaration {






    private Expression expression;


    public vhdl_declaration_FreeQuantityDeclaration(
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
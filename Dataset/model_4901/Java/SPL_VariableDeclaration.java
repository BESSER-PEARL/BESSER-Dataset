





import java.util.List;
import java.util.ArrayList;

public class SPL_VariableDeclaration extends Declaration {






    private SPL_TypeExpression spl_typeexpression;




    private SPL_Expression spl_expression;


    public SPL_VariableDeclaration(
    ) {
        super(
        );
    }



    public SPL_TypeExpression getSpl_typeexpression() {
        return spl_typeexpression;
    }

    public void setSpl_typeexpression(SPL_TypeExpression spl_typeexpression) {
        this.spl_typeexpression = spl_typeexpression;
    }
    public SPL_Expression getSpl_expression() {
        return spl_expression;
    }

    public void setSpl_expression(SPL_Expression spl_expression) {
        this.spl_expression = spl_expression;
    }

}
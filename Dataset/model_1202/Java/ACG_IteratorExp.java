





import java.util.List;
import java.util.ArrayList;

public class ACG_IteratorExp extends PropertyCallExp {






    private Expression expression;




    private VariableDecl variabledecl;


    public ACG_IteratorExp(
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
    public VariableDecl getVariabledecl() {
        return variabledecl;
    }

    public void setVariabledecl(VariableDecl variabledecl) {
        this.variabledecl = variabledecl;
    }

}
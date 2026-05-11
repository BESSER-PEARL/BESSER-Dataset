





import java.util.List;
import java.util.ArrayList;

public class plsql_expression_SQLVariable extends VarRefExpression {






    private VariableDeclaration variabledeclaration;


    public plsql_expression_SQLVariable(
    ) {
        super(
        );
    }



    public VariableDeclaration getVariabledeclaration() {
        return variabledeclaration;
    }

    public void setVariabledeclaration(VariableDeclaration variabledeclaration) {
        this.variabledeclaration = variabledeclaration;
    }

}
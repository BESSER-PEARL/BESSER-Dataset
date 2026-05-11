





import java.util.List;
import java.util.ArrayList;

public class ast_DerivativeOperator extends Expression {






    private ast_CallableElement ast_callableelement;


    public ast_DerivativeOperator(
    ) {
        super(
        );
    }



    public ast_CallableElement getAst_callableelement() {
        return ast_callableelement;
    }

    public void setAst_callableelement(ast_CallableElement ast_callableelement) {
        this.ast_callableelement = ast_callableelement;
    }

}






import java.util.List;
import java.util.ArrayList;

public class ast_Compound extends Statement {






    private ast_AlgorithmExpression ast_algorithmexpression;


    public ast_Compound(
    ) {
        super(
        );
    }



    public ast_AlgorithmExpression getAst_algorithmexpression() {
        return ast_algorithmexpression;
    }

    public void setAst_algorithmexpression(ast_AlgorithmExpression ast_algorithmexpression) {
        this.ast_algorithmexpression = ast_algorithmexpression;
    }

}
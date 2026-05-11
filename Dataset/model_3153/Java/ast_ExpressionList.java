





import java.util.List;
import java.util.ArrayList;

public class ast_ExpressionList  {






    private ast_ArrayConcatenationOperator ast_arrayconcatenationoperator;




    private List<ast_Expression> ast_expressions;


    public ast_ExpressionList(
    ) {
        this.ast_expressions = new ArrayList<>();
    }

    public ast_ExpressionList(
        ArrayList<ast_Expression> ast_expressions    ) {
        this.ast_expressions = ast_expressions;
    }


    public ast_ArrayConcatenationOperator getAst_arrayconcatenationoperator() {
        return ast_arrayconcatenationoperator;
    }

    public void setAst_arrayconcatenationoperator(ast_ArrayConcatenationOperator ast_arrayconcatenationoperator) {
        this.ast_arrayconcatenationoperator = ast_arrayconcatenationoperator;
    }
    public List<ast_Expression> getAst_expressions() {
        return ast_expressions;
    }

    public void addAst_expression(Ast_expression ast_expression) {
        this.ast_expressions.add(ast_expression);
    }

}
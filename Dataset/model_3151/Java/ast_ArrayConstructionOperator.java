





import java.util.List;
import java.util.ArrayList;

public class ast_ArrayConstructionOperator extends Expression {






    private List<ast_Expression> ast_expressions;


    public ast_ArrayConstructionOperator(
    ) {
        super(
        );
        this.ast_expressions = new ArrayList<>();
    }

    public ast_ArrayConstructionOperator(
        ArrayList<ast_Expression> ast_expressions    ) {
        this.ast_expressions = ast_expressions;
    }


    public List<ast_Expression> getAst_expressions() {
        return ast_expressions;
    }

    public void addAst_expression(Ast_expression ast_expression) {
        this.ast_expressions.add(ast_expression);
    }

}
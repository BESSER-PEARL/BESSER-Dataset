





import java.util.List;
import java.util.ArrayList;

public class ast_NewOp extends Expression {






    private ast_Expression ast_expression;




    private List<ast_Expression> ast_expressions;




    private ast_ClassBlock ast_classblock;


    public ast_NewOp(
    ) {
        super(
        );
        this.ast_expressions = new ArrayList<>();
    }

    public ast_NewOp(
        ArrayList<ast_Expression> ast_expressions    ) {
        this.ast_expressions = ast_expressions;
    }


    public ast_Expression getAst_expression() {
        return ast_expression;
    }

    public void setAst_expression(ast_Expression ast_expression) {
        this.ast_expression = ast_expression;
    }
    public List<ast_Expression> getAst_expressions() {
        return ast_expressions;
    }

    public void addAst_expression(Ast_expression ast_expression) {
        this.ast_expressions.add(ast_expression);
    }
    public ast_ClassBlock getAst_classblock() {
        return ast_classblock;
    }

    public void setAst_classblock(ast_ClassBlock ast_classblock) {
        this.ast_classblock = ast_classblock;
    }

}
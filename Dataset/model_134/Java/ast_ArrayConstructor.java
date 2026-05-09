





import java.util.List;
import java.util.ArrayList;

public class ast_ArrayConstructor extends Expression {






    private List<ast_Expression> ast_expressions;




    private ast_NewOp ast_newop;


    public ast_ArrayConstructor(
    ) {
        super(
        );
        this.ast_expressions = new ArrayList<>();
    }

    public ast_ArrayConstructor(
        ArrayList<ast_Expression> ast_expressions    ) {
        this.ast_expressions = ast_expressions;
    }


    public List<ast_Expression> getAst_expressions() {
        return ast_expressions;
    }

    public void addAst_expression(Ast_expression ast_expression) {
        this.ast_expressions.add(ast_expression);
    }
    public ast_NewOp getAst_newop() {
        return ast_newop;
    }

    public void setAst_newop(ast_NewOp ast_newop) {
        this.ast_newop = ast_newop;
    }

}
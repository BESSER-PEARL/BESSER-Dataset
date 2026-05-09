





import java.util.List;
import java.util.ArrayList;

public class ast_SuperConstructorInvocation extends Statement {






    private List<ast_Expression> ast_expressions;




    private ast_Expression ast_expression;




    private List<ast_Type> ast_types;


    public ast_SuperConstructorInvocation(
    ) {
        super(
        );
        this.ast_expressions = new ArrayList<>();
        this.ast_types = new ArrayList<>();
    }

    public ast_SuperConstructorInvocation(
        ArrayList<ast_Expression> ast_expressions,        ArrayList<ast_Type> ast_types    ) {
        this.ast_expressions = ast_expressions;
        this.ast_types = ast_types;
    }


    public List<ast_Expression> getAst_expressions() {
        return ast_expressions;
    }

    public void addAst_expression(Ast_expression ast_expression) {
        this.ast_expressions.add(ast_expression);
    }
    public ast_Expression getAst_expression() {
        return ast_expression;
    }

    public void setAst_expression(ast_Expression ast_expression) {
        this.ast_expression = ast_expression;
    }
    public List<ast_Type> getAst_types() {
        return ast_types;
    }

    public void addAst_type(Ast_type ast_type) {
        this.ast_types.add(ast_type);
    }

}
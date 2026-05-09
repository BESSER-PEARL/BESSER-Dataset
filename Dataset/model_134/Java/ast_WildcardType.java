





import java.util.List;
import java.util.ArrayList;

public class ast_WildcardType extends Expression {






    private List<ast_Expression> ast_expressions;




    private List<ast_Expression> ast_expressions;


    public ast_WildcardType(
    ) {
        super(
        );
        this.ast_expressions = new ArrayList<>();
        this.ast_expressions = new ArrayList<>();
    }

    public ast_WildcardType(
        ArrayList<ast_Expression> ast_expressions,        ArrayList<ast_Expression> ast_expressions    ) {
        this.ast_expressions = ast_expressions;
        this.ast_expressions = ast_expressions;
    }


    public List<ast_Expression> getAst_expressions() {
        return ast_expressions;
    }

    public void addAst_expression(Ast_expression ast_expression) {
        this.ast_expressions.add(ast_expression);
    }
    public List<ast_Expression> getAst_expressions() {
        return ast_expressions;
    }

    public void addAst_expression(Ast_expression ast_expression) {
        this.ast_expressions.add(ast_expression);
    }

}
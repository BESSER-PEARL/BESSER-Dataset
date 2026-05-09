





import java.util.List;
import java.util.ArrayList;

public class ast_ExpressionMethodReference extends MethodReference {






    private ast_SimpleName ast_simplename;




    private List<ast_Type> ast_types;




    private ast_Expression ast_expression;


    public ast_ExpressionMethodReference(
    ) {
        super(
        );
        this.ast_types = new ArrayList<>();
    }

    public ast_ExpressionMethodReference(
        ArrayList<ast_Type> ast_types    ) {
        this.ast_types = ast_types;
    }


    public ast_SimpleName getAst_simplename() {
        return ast_simplename;
    }

    public void setAst_simplename(ast_SimpleName ast_simplename) {
        this.ast_simplename = ast_simplename;
    }
    public List<ast_Type> getAst_types() {
        return ast_types;
    }

    public void addAst_type(Ast_type ast_type) {
        this.ast_types.add(ast_type);
    }
    public ast_Expression getAst_expression() {
        return ast_expression;
    }

    public void setAst_expression(ast_Expression ast_expression) {
        this.ast_expression = ast_expression;
    }

}
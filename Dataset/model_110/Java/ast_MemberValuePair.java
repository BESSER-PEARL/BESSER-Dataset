





import java.util.List;
import java.util.ArrayList;

public class ast_MemberValuePair extends ASTNode {






    private ast_Expression ast_expression;




    private ast_NormalAnnotation ast_normalannotation;


    public ast_MemberValuePair(
    ) {
        super(
        );
    }



    public ast_Expression getAst_expression() {
        return ast_expression;
    }

    public void setAst_expression(ast_Expression ast_expression) {
        this.ast_expression = ast_expression;
    }
    public ast_NormalAnnotation getAst_normalannotation() {
        return ast_normalannotation;
    }

    public void setAst_normalannotation(ast_NormalAnnotation ast_normalannotation) {
        this.ast_normalannotation = ast_normalannotation;
    }

}
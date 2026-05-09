





import java.util.List;
import java.util.ArrayList;

public class ast_Parameter extends NamedElement {






    private ast_Expression ast_expression;




    private ast_Modifier ast_modifier;


    public ast_Parameter(
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
    public ast_Modifier getAst_modifier() {
        return ast_modifier;
    }

    public void setAst_modifier(ast_Modifier ast_modifier) {
        this.ast_modifier = ast_modifier;
    }

}
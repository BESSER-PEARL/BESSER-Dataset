





import java.util.List;
import java.util.ArrayList;

public class ast_FieldStatement extends Feature {






    private ast_Modifier ast_modifier;




    private ast_Modifier ast_modifier;




    private List<ast_Variable> ast_variables;




    private ast_Expression ast_expression;


    public ast_FieldStatement(
    ) {
        super(
        );
        this.ast_variables = new ArrayList<>();
    }

    public ast_FieldStatement(
        ArrayList<ast_Variable> ast_variables    ) {
        this.ast_variables = ast_variables;
    }


    public ast_Modifier getAst_modifier() {
        return ast_modifier;
    }

    public void setAst_modifier(ast_Modifier ast_modifier) {
        this.ast_modifier = ast_modifier;
    }
    public ast_Modifier getAst_modifier() {
        return ast_modifier;
    }

    public void setAst_modifier(ast_Modifier ast_modifier) {
        this.ast_modifier = ast_modifier;
    }
    public List<ast_Variable> getAst_variables() {
        return ast_variables;
    }

    public void addAst_variable(Ast_variable ast_variable) {
        this.ast_variables.add(ast_variable);
    }
    public ast_Expression getAst_expression() {
        return ast_expression;
    }

    public void setAst_expression(ast_Expression ast_expression) {
        this.ast_expression = ast_expression;
    }

}
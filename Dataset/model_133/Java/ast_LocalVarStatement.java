





import java.util.List;
import java.util.ArrayList;

public class ast_LocalVarStatement extends MethodContentStatement {






    private ast_ForStatement ast_forstatement;




    private ast_Modifier ast_modifier;




    private List<ast_Variable> ast_variables;




    private ast_Expression ast_expression;


    public ast_LocalVarStatement(
    ) {
        super(
        );
        this.ast_variables = new ArrayList<>();
    }

    public ast_LocalVarStatement(
        ArrayList<ast_Variable> ast_variables    ) {
        this.ast_variables = ast_variables;
    }


    public ast_ForStatement getAst_forstatement() {
        return ast_forstatement;
    }

    public void setAst_forstatement(ast_ForStatement ast_forstatement) {
        this.ast_forstatement = ast_forstatement;
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
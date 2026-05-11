





import java.util.List;
import java.util.ArrayList;

public class ast_Equation  {

    private boolean initial;





    private ast_FunctionDefinition ast_functiondefinition;




    private ast_Expression ast_expression;




    private ast_Expression ast_expression;


    public ast_Equation(
        boolean initial    ) {
        this.initial = initial;
    }


    public boolean getInitial() {
        return initial;
    }

    public void setInitial(boolean initial) {
        this.initial = initial;
    }

    public ast_FunctionDefinition getAst_functiondefinition() {
        return ast_functiondefinition;
    }

    public void setAst_functiondefinition(ast_FunctionDefinition ast_functiondefinition) {
        this.ast_functiondefinition = ast_functiondefinition;
    }
    public ast_Expression getAst_expression() {
        return ast_expression;
    }

    public void setAst_expression(ast_Expression ast_expression) {
        this.ast_expression = ast_expression;
    }
    public ast_Expression getAst_expression() {
        return ast_expression;
    }

    public void setAst_expression(ast_Expression ast_expression) {
        this.ast_expression = ast_expression;
    }

}
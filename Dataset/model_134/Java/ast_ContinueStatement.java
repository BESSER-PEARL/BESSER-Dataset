





import java.util.List;
import java.util.ArrayList;

public class ast_ContinueStatement extends JumpStatement {






    private ast_SwitchDefaultPartRef ast_switchdefaultpartref;




    private ast_Expression ast_expression;


    public ast_ContinueStatement(
    ) {
        super(
        );
    }



    public ast_SwitchDefaultPartRef getAst_switchdefaultpartref() {
        return ast_switchdefaultpartref;
    }

    public void setAst_switchdefaultpartref(ast_SwitchDefaultPartRef ast_switchdefaultpartref) {
        this.ast_switchdefaultpartref = ast_switchdefaultpartref;
    }
    public ast_Expression getAst_expression() {
        return ast_expression;
    }

    public void setAst_expression(ast_Expression ast_expression) {
        this.ast_expression = ast_expression;
    }

}
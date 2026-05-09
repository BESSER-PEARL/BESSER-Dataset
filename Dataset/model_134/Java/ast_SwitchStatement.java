





import java.util.List;
import java.util.ArrayList;

public class ast_SwitchStatement extends LabeledStatement {






    private ast_Expression ast_expression;




    private List<ast_SwitchPart> ast_switchparts;


    public ast_SwitchStatement(
    ) {
        super(
        );
        this.ast_switchparts = new ArrayList<>();
    }

    public ast_SwitchStatement(
        ArrayList<ast_SwitchPart> ast_switchparts    ) {
        this.ast_switchparts = ast_switchparts;
    }


    public ast_Expression getAst_expression() {
        return ast_expression;
    }

    public void setAst_expression(ast_Expression ast_expression) {
        this.ast_expression = ast_expression;
    }
    public List<ast_SwitchPart> getAst_switchparts() {
        return ast_switchparts;
    }

    public void addAst_switchpart(Ast_switchpart ast_switchpart) {
        this.ast_switchparts.add(ast_switchpart);
    }

}
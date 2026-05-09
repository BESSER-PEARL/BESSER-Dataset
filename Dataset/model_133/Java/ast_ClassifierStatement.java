





import java.util.List;
import java.util.ArrayList;

public class ast_ClassifierStatement extends EJBase {






    private List<ast_TemplateParameter> ast_templateparameters;




    private ast_Modifier ast_modifier;




    private ast_Identifier ast_identifier;


    public ast_ClassifierStatement(
    ) {
        super(
        );
        this.ast_templateparameters = new ArrayList<>();
    }

    public ast_ClassifierStatement(
        ArrayList<ast_TemplateParameter> ast_templateparameters    ) {
        this.ast_templateparameters = ast_templateparameters;
    }


    public List<ast_TemplateParameter> getAst_templateparameters() {
        return ast_templateparameters;
    }

    public void addAst_templateparameter(Ast_templateparameter ast_templateparameter) {
        this.ast_templateparameters.add(ast_templateparameter);
    }
    public ast_Modifier getAst_modifier() {
        return ast_modifier;
    }

    public void setAst_modifier(ast_Modifier ast_modifier) {
        this.ast_modifier = ast_modifier;
    }
    public ast_Identifier getAst_identifier() {
        return ast_identifier;
    }

    public void setAst_identifier(ast_Identifier ast_identifier) {
        this.ast_identifier = ast_identifier;
    }

}
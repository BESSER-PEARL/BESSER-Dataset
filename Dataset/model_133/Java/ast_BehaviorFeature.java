





import java.util.List;
import java.util.ArrayList;

public class ast_BehaviorFeature extends Feature {






    private List<ast_TemplateParameter> ast_templateparameters;




    private ast_Identifier ast_identifier;




    private List<ast_Parameter> ast_parameters;




    private List<ast_Expression> ast_expressions;


    public ast_BehaviorFeature(
    ) {
        super(
        );
        this.ast_templateparameters = new ArrayList<>();
        this.ast_parameters = new ArrayList<>();
        this.ast_expressions = new ArrayList<>();
    }

    public ast_BehaviorFeature(
        ArrayList<ast_TemplateParameter> ast_templateparameters,        ArrayList<ast_Parameter> ast_parameters,        ArrayList<ast_Expression> ast_expressions    ) {
        this.ast_templateparameters = ast_templateparameters;
        this.ast_parameters = ast_parameters;
        this.ast_expressions = ast_expressions;
    }


    public List<ast_TemplateParameter> getAst_templateparameters() {
        return ast_templateparameters;
    }

    public void addAst_templateparameter(Ast_templateparameter ast_templateparameter) {
        this.ast_templateparameters.add(ast_templateparameter);
    }
    public ast_Identifier getAst_identifier() {
        return ast_identifier;
    }

    public void setAst_identifier(ast_Identifier ast_identifier) {
        this.ast_identifier = ast_identifier;
    }
    public List<ast_Parameter> getAst_parameters() {
        return ast_parameters;
    }

    public void addAst_parameter(Ast_parameter ast_parameter) {
        this.ast_parameters.add(ast_parameter);
    }
    public List<ast_Expression> getAst_expressions() {
        return ast_expressions;
    }

    public void addAst_expression(Ast_expression ast_expression) {
        this.ast_expressions.add(ast_expression);
    }

}
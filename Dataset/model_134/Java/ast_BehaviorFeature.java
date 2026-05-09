





import java.util.List;
import java.util.ArrayList;

public class ast_BehaviorFeature extends Feature {






    private List<ast_Parameter> ast_parameters;




    private List<ast_Expression> ast_expressions;




    private List<ast_TemplateParameter> ast_templateparameters;


    public ast_BehaviorFeature(
    ) {
        super(
        );
        this.ast_parameters = new ArrayList<>();
        this.ast_expressions = new ArrayList<>();
        this.ast_templateparameters = new ArrayList<>();
    }

    public ast_BehaviorFeature(
        ArrayList<ast_Parameter> ast_parameters,        ArrayList<ast_Expression> ast_expressions,        ArrayList<ast_TemplateParameter> ast_templateparameters    ) {
        this.ast_parameters = ast_parameters;
        this.ast_expressions = ast_expressions;
        this.ast_templateparameters = ast_templateparameters;
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
    public List<ast_TemplateParameter> getAst_templateparameters() {
        return ast_templateparameters;
    }

    public void addAst_templateparameter(Ast_templateparameter ast_templateparameter) {
        this.ast_templateparameters.add(ast_templateparameter);
    }

}
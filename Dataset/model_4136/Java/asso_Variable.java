





import java.util.List;
import java.util.ArrayList;

public class asso_Variable  {

    private String name;





    private asso_VariableRef asso_variableref;




    private asso_Expression asso_expression;




    private asso_Model asso_model;




    private List<asso_Variable> asso_variables;


    public asso_Variable(
        String name    ) {
        this.name = name;
        this.asso_variables = new ArrayList<>();
    }

    public asso_Variable(
        String name        ArrayList<asso_Variable> asso_variables    ) {
        this.name = name;
        this.asso_variables = asso_variables;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public asso_VariableRef getAsso_variableref() {
        return asso_variableref;
    }

    public void setAsso_variableref(asso_VariableRef asso_variableref) {
        this.asso_variableref = asso_variableref;
    }
    public asso_Expression getAsso_expression() {
        return asso_expression;
    }

    public void setAsso_expression(asso_Expression asso_expression) {
        this.asso_expression = asso_expression;
    }
    public asso_Model getAsso_model() {
        return asso_model;
    }

    public void setAsso_model(asso_Model asso_model) {
        this.asso_model = asso_model;
    }
    public List<asso_Variable> getAsso_variables() {
        return asso_variables;
    }

    public void addAsso_variable(Asso_variable asso_variable) {
        this.asso_variables.add(asso_variable);
    }

}






import java.util.List;
import java.util.ArrayList;

public class essentialocl_expressions_ExpressionInOcl extends Expression {






    private Variable variable;




    private OclExpression oclexpression;




    private List<Variable> variables;




    private Variable variable;


    public essentialocl_expressions_ExpressionInOcl(
    ) {
        super(
        );
        this.variables = new ArrayList<>();
    }

    public essentialocl_expressions_ExpressionInOcl(
        ArrayList<Variable> variables    ) {
        this.variables = variables;
    }


    public Variable getVariable() {
        return variable;
    }

    public void setVariable(Variable variable) {
        this.variable = variable;
    }
    public OclExpression getOclexpression() {
        return oclexpression;
    }

    public void setOclexpression(OclExpression oclexpression) {
        this.oclexpression = oclexpression;
    }
    public List<Variable> getVariables() {
        return variables;
    }

    public void addVariable(Variable variable) {
        this.variables.add(variable);
    }
    public Variable getVariable() {
        return variable;
    }

    public void setVariable(Variable variable) {
        this.variable = variable;
    }

}






import java.util.List;
import java.util.ArrayList;

public class transformr_Expression  {

    private String expression;





    private List<transformr_Variable> transformr_variables;


    public transformr_Expression(
        String expression    ) {
        this.expression = expression;
        this.transformr_variables = new ArrayList<>();
    }

    public transformr_Expression(
        String expression        ArrayList<transformr_Variable> transformr_variables    ) {
        this.expression = expression;
        this.transformr_variables = transformr_variables;
    }

    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }

    public List<transformr_Variable> getTransformr_variables() {
        return transformr_variables;
    }

    public void addTransformr_variable(Transformr_variable transformr_variable) {
        this.transformr_variables.add(transformr_variable);
    }

}
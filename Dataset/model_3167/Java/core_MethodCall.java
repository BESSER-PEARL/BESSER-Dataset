





import java.util.List;
import java.util.ArrayList;

public class core_MethodCall extends Expression {

    private boolean withParameters;
    private String methodName;





    private List<core_Expression> core_expressions;




    private core_Expression core_expression;


    public core_MethodCall(
        boolean withParameters,        String methodName    ) {
        super(
        );
        this.withParameters = withParameters;
        this.methodName = methodName;
        this.core_expressions = new ArrayList<>();
    }

    public core_MethodCall(
        boolean withParameters,        String methodName        ArrayList<core_Expression> core_expressions    ) {
        this.withParameters = withParameters;
        this.methodName = methodName;
        this.core_expressions = core_expressions;
    }

    public boolean getWithparameters() {
        return withParameters;
    }

    public void setWithparameters(boolean withParameters) {
        this.withParameters = withParameters;
    }
    public String getMethodname() {
        return methodName;
    }

    public void setMethodname(String methodName) {
        this.methodName = methodName;
    }

    public List<core_Expression> getCore_expressions() {
        return core_expressions;
    }

    public void addCore_expression(Core_expression core_expression) {
        this.core_expressions.add(core_expression);
    }
    public core_Expression getCore_expression() {
        return core_expression;
    }

    public void setCore_expression(core_Expression core_expression) {
        this.core_expression = core_expression;
    }

}
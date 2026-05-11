





import java.util.List;
import java.util.ArrayList;

public class camel_metric_MetricFormula extends MetricFormulaParameter {

    private String function;
    private String functionArity;
    private String functionPattern;



    public camel_metric_MetricFormula(
        String function,        String functionArity,        String functionPattern    ) {
        super(
        );
        this.function = function;
        this.functionArity = functionArity;
        this.functionPattern = functionPattern;
    }


    public String getFunction() {
        return function;
    }

    public void setFunction(String function) {
        this.function = function;
    }
    public String getFunctionarity() {
        return functionArity;
    }

    public void setFunctionarity(String functionArity) {
        this.functionArity = functionArity;
    }
    public String getFunctionpattern() {
        return functionPattern;
    }

    public void setFunctionpattern(String functionPattern) {
        this.functionPattern = functionPattern;
    }


}
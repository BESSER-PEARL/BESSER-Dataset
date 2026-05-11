





import java.util.List;
import java.util.ArrayList;

public class OPLmetamodel_FunctionCall extends PathExpression {

    private String functionName;





    private List<OPLmetamodel_Expression> oplmetamodel_expressions;


    public OPLmetamodel_FunctionCall(
        String functionName    ) {
        super(
        );
        this.functionName = functionName;
        this.oplmetamodel_expressions = new ArrayList<>();
    }

    public OPLmetamodel_FunctionCall(
        String functionName        ArrayList<OPLmetamodel_Expression> oplmetamodel_expressions    ) {
        this.functionName = functionName;
        this.oplmetamodel_expressions = oplmetamodel_expressions;
    }

    public String getFunctionname() {
        return functionName;
    }

    public void setFunctionname(String functionName) {
        this.functionName = functionName;
    }

    public List<OPLmetamodel_Expression> getOplmetamodel_expressions() {
        return oplmetamodel_expressions;
    }

    public void addOplmetamodel_expression(Oplmetamodel_expression oplmetamodel_expression) {
        this.oplmetamodel_expressions.add(oplmetamodel_expression);
    }

}
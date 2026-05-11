





import java.util.List;
import java.util.ArrayList;

public class frontend_qool_InvokeExternal extends InvokeTransformation {

    private String traceAttributeName;
    private String queueName;





    private Expression expression;


    public frontend_qool_InvokeExternal(
        String traceAttributeName,        String queueName    ) {
        super(
        );
        this.traceAttributeName = traceAttributeName;
        this.queueName = queueName;
    }


    public String getTraceattributename() {
        return traceAttributeName;
    }

    public void setTraceattributename(String traceAttributeName) {
        this.traceAttributeName = traceAttributeName;
    }
    public String getQueuename() {
        return queueName;
    }

    public void setQueuename(String queueName) {
        this.queueName = queueName;
    }

    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }

}
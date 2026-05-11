





import java.util.List;
import java.util.ArrayList;

public class iotdsl_EventOccurrence extends Expression {

    private String operator;





    private iotdsl_Value iotdsl_value;




    private iotdsl_NodeInstance iotdsl_nodeinstance;




    private iotdsl_NotExpression iotdsl_notexpression;




    private iotdsl_Sensing iotdsl_sensing;


    public iotdsl_EventOccurrence(
        String operator    ) {
        super(
        );
        this.operator = operator;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public iotdsl_Value getIotdsl_value() {
        return iotdsl_value;
    }

    public void setIotdsl_value(iotdsl_Value iotdsl_value) {
        this.iotdsl_value = iotdsl_value;
    }
    public iotdsl_NodeInstance getIotdsl_nodeinstance() {
        return iotdsl_nodeinstance;
    }

    public void setIotdsl_nodeinstance(iotdsl_NodeInstance iotdsl_nodeinstance) {
        this.iotdsl_nodeinstance = iotdsl_nodeinstance;
    }
    public iotdsl_NotExpression getIotdsl_notexpression() {
        return iotdsl_notexpression;
    }

    public void setIotdsl_notexpression(iotdsl_NotExpression iotdsl_notexpression) {
        this.iotdsl_notexpression = iotdsl_notexpression;
    }
    public iotdsl_Sensing getIotdsl_sensing() {
        return iotdsl_sensing;
    }

    public void setIotdsl_sensing(iotdsl_Sensing iotdsl_sensing) {
        this.iotdsl_sensing = iotdsl_sensing;
    }

}
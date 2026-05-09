





import java.util.List;
import java.util.ArrayList;

public class dsl_RelationalExpression  {

    private String ops;





    private dsl_InstanceOfExpression dsl_instanceofexpression;


    public dsl_RelationalExpression(
        String ops    ) {
        this.ops = ops;
    }


    public String getOps() {
        return ops;
    }

    public void setOps(String ops) {
        this.ops = ops;
    }

    public dsl_InstanceOfExpression getDsl_instanceofexpression() {
        return dsl_instanceofexpression;
    }

    public void setDsl_instanceofexpression(dsl_InstanceOfExpression dsl_instanceofexpression) {
        this.dsl_instanceofexpression = dsl_instanceofexpression;
    }

}
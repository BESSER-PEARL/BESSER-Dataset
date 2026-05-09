





import java.util.List;
import java.util.ArrayList;

public class dsl_ShiftExpression  {

    private String ops;





    private dsl_RelationalExpression dsl_relationalexpression;


    public dsl_ShiftExpression(
        String ops    ) {
        this.ops = ops;
    }


    public String getOps() {
        return ops;
    }

    public void setOps(String ops) {
        this.ops = ops;
    }

    public dsl_RelationalExpression getDsl_relationalexpression() {
        return dsl_relationalexpression;
    }

    public void setDsl_relationalexpression(dsl_RelationalExpression dsl_relationalexpression) {
        this.dsl_relationalexpression = dsl_relationalexpression;
    }

}
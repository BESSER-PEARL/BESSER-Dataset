





import java.util.List;
import java.util.ArrayList;

public class dsl_AdditiveExpression  {

    private String ops;





    private dsl_ShiftExpression dsl_shiftexpression;


    public dsl_AdditiveExpression(
        String ops    ) {
        this.ops = ops;
    }


    public String getOps() {
        return ops;
    }

    public void setOps(String ops) {
        this.ops = ops;
    }

    public dsl_ShiftExpression getDsl_shiftexpression() {
        return dsl_shiftexpression;
    }

    public void setDsl_shiftexpression(dsl_ShiftExpression dsl_shiftexpression) {
        this.dsl_shiftexpression = dsl_shiftexpression;
    }

}
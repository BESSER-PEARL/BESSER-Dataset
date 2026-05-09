





import java.util.List;
import java.util.ArrayList;

public class dsl_MultiplicativeExpression  {

    private String ops;





    private dsl_AdditiveExpression dsl_additiveexpression;


    public dsl_MultiplicativeExpression(
        String ops    ) {
        this.ops = ops;
    }


    public String getOps() {
        return ops;
    }

    public void setOps(String ops) {
        this.ops = ops;
    }

    public dsl_AdditiveExpression getDsl_additiveexpression() {
        return dsl_additiveexpression;
    }

    public void setDsl_additiveexpression(dsl_AdditiveExpression dsl_additiveexpression) {
        this.dsl_additiveexpression = dsl_additiveexpression;
    }

}
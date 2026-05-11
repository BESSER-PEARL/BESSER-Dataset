





import java.util.List;
import java.util.ArrayList;

public class swrtj_AtomicBooleanExpression  {

    private boolean negated;





    private swrtj_BooleanExpression swrtj_booleanexpression;


    public swrtj_AtomicBooleanExpression(
        boolean negated    ) {
        this.negated = negated;
    }


    public boolean getNegated() {
        return negated;
    }

    public void setNegated(boolean negated) {
        this.negated = negated;
    }

    public swrtj_BooleanExpression getSwrtj_booleanexpression() {
        return swrtj_booleanexpression;
    }

    public void setSwrtj_booleanexpression(swrtj_BooleanExpression swrtj_booleanexpression) {
        this.swrtj_booleanexpression = swrtj_booleanexpression;
    }

}
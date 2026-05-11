





import java.util.List;
import java.util.ArrayList;

public class alf_AdditiveExpression  {

    private String op;





    private alf_ShiftExpression alf_shiftexpression;


    public alf_AdditiveExpression(
        String op    ) {
        this.op = op;
    }


    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public alf_ShiftExpression getAlf_shiftexpression() {
        return alf_shiftexpression;
    }

    public void setAlf_shiftexpression(alf_ShiftExpression alf_shiftexpression) {
        this.alf_shiftexpression = alf_shiftexpression;
    }

}






import java.util.List;
import java.util.ArrayList;

public class alf_UnaryExpression  {

    private String op;





    private alf_MultiplicativeExpression alf_multiplicativeexpression;


    public alf_UnaryExpression(
        String op    ) {
        this.op = op;
    }


    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public alf_MultiplicativeExpression getAlf_multiplicativeexpression() {
        return alf_multiplicativeexpression;
    }

    public void setAlf_multiplicativeexpression(alf_MultiplicativeExpression alf_multiplicativeexpression) {
        this.alf_multiplicativeexpression = alf_multiplicativeexpression;
    }

}
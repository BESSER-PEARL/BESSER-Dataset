





import java.util.List;
import java.util.ArrayList;

public class alf_MultiplicativeExpression  {

    private String op;





    private alf_AdditiveExpression alf_additiveexpression;


    public alf_MultiplicativeExpression(
        String op    ) {
        this.op = op;
    }


    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public alf_AdditiveExpression getAlf_additiveexpression() {
        return alf_additiveexpression;
    }

    public void setAlf_additiveexpression(alf_AdditiveExpression alf_additiveexpression) {
        this.alf_additiveexpression = alf_additiveexpression;
    }

}
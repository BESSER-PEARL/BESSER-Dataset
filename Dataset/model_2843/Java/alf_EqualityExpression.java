





import java.util.List;
import java.util.ArrayList;

public class alf_EqualityExpression  {

    private String op;





    private alf_AndExpression alf_andexpression;


    public alf_EqualityExpression(
        String op    ) {
        this.op = op;
    }


    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public alf_AndExpression getAlf_andexpression() {
        return alf_andexpression;
    }

    public void setAlf_andexpression(alf_AndExpression alf_andexpression) {
        this.alf_andexpression = alf_andexpression;
    }

}






import java.util.List;
import java.util.ArrayList;

public class alf_ClassificationExpression  {

    private String op;





    private alf_EqualityExpression alf_equalityexpression;




    private alf_NameExpression alf_nameexpression;


    public alf_ClassificationExpression(
        String op    ) {
        this.op = op;
    }


    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public alf_EqualityExpression getAlf_equalityexpression() {
        return alf_equalityexpression;
    }

    public void setAlf_equalityexpression(alf_EqualityExpression alf_equalityexpression) {
        this.alf_equalityexpression = alf_equalityexpression;
    }
    public alf_NameExpression getAlf_nameexpression() {
        return alf_nameexpression;
    }

    public void setAlf_nameexpression(alf_NameExpression alf_nameexpression) {
        this.alf_nameexpression = alf_nameexpression;
    }

}
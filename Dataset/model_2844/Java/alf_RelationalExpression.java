





import java.util.List;
import java.util.ArrayList;

public class alf_RelationalExpression  {

    private String op;





    private alf_ClassificationExpression alf_classificationexpression;


    public alf_RelationalExpression(
        String op    ) {
        this.op = op;
    }


    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public alf_ClassificationExpression getAlf_classificationexpression() {
        return alf_classificationexpression;
    }

    public void setAlf_classificationexpression(alf_ClassificationExpression alf_classificationexpression) {
        this.alf_classificationexpression = alf_classificationexpression;
    }

}
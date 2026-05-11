





import java.util.List;
import java.util.ArrayList;

public class alf_ShiftExpression  {

    private String op;





    private alf_RelationalExpression alf_relationalexpression;




    private List<alf_AdditiveExpression> alf_additiveexpressions;




    private alf_RelationalExpression alf_relationalexpression;


    public alf_ShiftExpression(
        String op    ) {
        this.op = op;
        this.alf_additiveexpressions = new ArrayList<>();
    }

    public alf_ShiftExpression(
        String op        ArrayList<alf_AdditiveExpression> alf_additiveexpressions    ) {
        this.op = op;
        this.alf_additiveexpressions = alf_additiveexpressions;
    }

    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public alf_RelationalExpression getAlf_relationalexpression() {
        return alf_relationalexpression;
    }

    public void setAlf_relationalexpression(alf_RelationalExpression alf_relationalexpression) {
        this.alf_relationalexpression = alf_relationalexpression;
    }
    public List<alf_AdditiveExpression> getAlf_additiveexpressions() {
        return alf_additiveexpressions;
    }

    public void addAlf_additiveexpression(Alf_additiveexpression alf_additiveexpression) {
        this.alf_additiveexpressions.add(alf_additiveexpression);
    }
    public alf_RelationalExpression getAlf_relationalexpression() {
        return alf_relationalexpression;
    }

    public void setAlf_relationalexpression(alf_RelationalExpression alf_relationalexpression) {
        this.alf_relationalexpression = alf_relationalexpression;
    }

}
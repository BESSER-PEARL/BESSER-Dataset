





import java.util.List;
import java.util.ArrayList;

public class alf_MultiplicativeExpression  {

    private String op;





    private List<alf_UnaryExpression> alf_unaryexpressions;




    private alf_AdditiveExpression alf_additiveexpression;


    public alf_MultiplicativeExpression(
        String op    ) {
        this.op = op;
        this.alf_unaryexpressions = new ArrayList<>();
    }

    public alf_MultiplicativeExpression(
        String op        ArrayList<alf_UnaryExpression> alf_unaryexpressions    ) {
        this.op = op;
        this.alf_unaryexpressions = alf_unaryexpressions;
    }

    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public List<alf_UnaryExpression> getAlf_unaryexpressions() {
        return alf_unaryexpressions;
    }

    public void addAlf_unaryexpression(Alf_unaryexpression alf_unaryexpression) {
        this.alf_unaryexpressions.add(alf_unaryexpression);
    }
    public alf_AdditiveExpression getAlf_additiveexpression() {
        return alf_additiveexpression;
    }

    public void setAlf_additiveexpression(alf_AdditiveExpression alf_additiveexpression) {
        this.alf_additiveexpression = alf_additiveexpression;
    }

}
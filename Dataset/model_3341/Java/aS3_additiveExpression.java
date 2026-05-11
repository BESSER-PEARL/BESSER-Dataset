





import java.util.List;
import java.util.ArrayList;

public class aS3_additiveExpression  {

    private String o;





    private List<aS3_multiplicativeExpression> as3_multiplicativeexpressions;




    private aS3_shiftExpression as3_shiftexpression;


    public aS3_additiveExpression(
        String o    ) {
        this.o = o;
        this.as3_multiplicativeexpressions = new ArrayList<>();
    }

    public aS3_additiveExpression(
        String o        ArrayList<aS3_multiplicativeExpression> as3_multiplicativeexpressions    ) {
        this.o = o;
        this.as3_multiplicativeexpressions = as3_multiplicativeexpressions;
    }

    public String getO() {
        return o;
    }

    public void setO(String o) {
        this.o = o;
    }

    public List<aS3_multiplicativeExpression> getAs3_multiplicativeexpressions() {
        return as3_multiplicativeexpressions;
    }

    public void addAs3_multiplicativeexpression(As3_multiplicativeexpression as3_multiplicativeexpression) {
        this.as3_multiplicativeexpressions.add(as3_multiplicativeexpression);
    }
    public aS3_shiftExpression getAs3_shiftexpression() {
        return as3_shiftexpression;
    }

    public void setAs3_shiftexpression(aS3_shiftExpression as3_shiftexpression) {
        this.as3_shiftexpression = as3_shiftexpression;
    }

}
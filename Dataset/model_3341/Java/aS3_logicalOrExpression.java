





import java.util.List;
import java.util.ArrayList;

public class aS3_logicalOrExpression extends conditionalExpression {

    private String o;





    private aS3_conditionalSubExpression as3_conditionalsubexpression;


    public aS3_logicalOrExpression(
        String o    ) {
        super(
        );
        this.o = o;
    }


    public String getO() {
        return o;
    }

    public void setO(String o) {
        this.o = o;
    }

    public aS3_conditionalSubExpression getAs3_conditionalsubexpression() {
        return as3_conditionalsubexpression;
    }

    public void setAs3_conditionalsubexpression(aS3_conditionalSubExpression as3_conditionalsubexpression) {
        this.as3_conditionalsubexpression = as3_conditionalsubexpression;
    }

}
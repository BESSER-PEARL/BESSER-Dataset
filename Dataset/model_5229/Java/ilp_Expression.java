





import java.util.List;
import java.util.ArrayList;

public class ilp_Expression  {

    private String comment;





    private ilp_BinaryExpression ilp_binaryexpression;




    private ilp_ObjectiveFunctionExpression ilp_objectivefunctionexpression;




    private ilp_BinaryExpression ilp_binaryexpression;


    public ilp_Expression(
        String comment    ) {
        this.comment = comment;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    public ilp_BinaryExpression getIlp_binaryexpression() {
        return ilp_binaryexpression;
    }

    public void setIlp_binaryexpression(ilp_BinaryExpression ilp_binaryexpression) {
        this.ilp_binaryexpression = ilp_binaryexpression;
    }
    public ilp_ObjectiveFunctionExpression getIlp_objectivefunctionexpression() {
        return ilp_objectivefunctionexpression;
    }

    public void setIlp_objectivefunctionexpression(ilp_ObjectiveFunctionExpression ilp_objectivefunctionexpression) {
        this.ilp_objectivefunctionexpression = ilp_objectivefunctionexpression;
    }
    public ilp_BinaryExpression getIlp_binaryexpression() {
        return ilp_binaryexpression;
    }

    public void setIlp_binaryexpression(ilp_BinaryExpression ilp_binaryexpression) {
        this.ilp_binaryexpression = ilp_binaryexpression;
    }

}
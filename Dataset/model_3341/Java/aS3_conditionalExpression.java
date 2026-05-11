





import java.util.List;
import java.util.ArrayList;

public class aS3_conditionalExpression extends assignmentExpression {

    private String op;





    private List<aS3_Expression> as3_expressions;


    public aS3_conditionalExpression(
        String op    ) {
        super(
        );
        this.op = op;
        this.as3_expressions = new ArrayList<>();
    }

    public aS3_conditionalExpression(
        String op        ArrayList<aS3_Expression> as3_expressions    ) {
        this.op = op;
        this.as3_expressions = as3_expressions;
    }

    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public List<aS3_Expression> getAs3_expressions() {
        return as3_expressions;
    }

    public void addAs3_expression(As3_expression as3_expression) {
        this.as3_expressions.add(as3_expression);
    }

}
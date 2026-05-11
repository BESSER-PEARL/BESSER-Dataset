





import java.util.List;
import java.util.ArrayList;

public class sADL_BinaryOperation extends Expression {

    private String op;





    private sADL_Expression sadl_expression;




    private sADL_Expression sadl_expression;


    public sADL_BinaryOperation(
        String op    ) {
        super(
        );
        this.op = op;
    }


    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public sADL_Expression getSadl_expression() {
        return sadl_expression;
    }

    public void setSadl_expression(sADL_Expression sadl_expression) {
        this.sadl_expression = sadl_expression;
    }
    public sADL_Expression getSadl_expression() {
        return sadl_expression;
    }

    public void setSadl_expression(sADL_Expression sadl_expression) {
        this.sadl_expression = sadl_expression;
    }

}






import java.util.List;
import java.util.ArrayList;

public class myDsl_unary_expression extends simple_expression {

    private String sizeof;
    private String inc_op;
    private String unary_operator;
    private String dec_op;
    private String alignof;





    private myDsl_assignment_expression mydsl_assignment_expression;




    private myDsl_unary_expression mydsl_unary_expression;




    private myDsl_postfix_expression mydsl_postfix_expression;


    public myDsl_unary_expression(
        String sizeof,        String inc_op,        String unary_operator,        String dec_op,        String alignof    ) {
        super(
        );
        this.sizeof = sizeof;
        this.inc_op = inc_op;
        this.unary_operator = unary_operator;
        this.dec_op = dec_op;
        this.alignof = alignof;
    }


    public String getSizeof() {
        return sizeof;
    }

    public void setSizeof(String sizeof) {
        this.sizeof = sizeof;
    }
    public String getInc_op() {
        return inc_op;
    }

    public void setInc_op(String inc_op) {
        this.inc_op = inc_op;
    }
    public String getUnary_operator() {
        return unary_operator;
    }

    public void setUnary_operator(String unary_operator) {
        this.unary_operator = unary_operator;
    }
    public String getDec_op() {
        return dec_op;
    }

    public void setDec_op(String dec_op) {
        this.dec_op = dec_op;
    }
    public String getAlignof() {
        return alignof;
    }

    public void setAlignof(String alignof) {
        this.alignof = alignof;
    }

    public myDsl_assignment_expression getMydsl_assignment_expression() {
        return mydsl_assignment_expression;
    }

    public void setMydsl_assignment_expression(myDsl_assignment_expression mydsl_assignment_expression) {
        this.mydsl_assignment_expression = mydsl_assignment_expression;
    }
    public myDsl_unary_expression getMydsl_unary_expression() {
        return mydsl_unary_expression;
    }

    public void setMydsl_unary_expression(myDsl_unary_expression mydsl_unary_expression) {
        this.mydsl_unary_expression = mydsl_unary_expression;
    }
    public myDsl_postfix_expression getMydsl_postfix_expression() {
        return mydsl_postfix_expression;
    }

    public void setMydsl_postfix_expression(myDsl_postfix_expression mydsl_postfix_expression) {
        this.mydsl_postfix_expression = mydsl_postfix_expression;
    }

}
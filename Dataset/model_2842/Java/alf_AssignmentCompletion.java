





import java.util.List;
import java.util.ArrayList;

public class alf_AssignmentCompletion  {

    private String op;





    private alf_Expression alf_expression;




    private alf_Test alf_test;


    public alf_AssignmentCompletion(
        String op    ) {
        this.op = op;
    }


    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public alf_Expression getAlf_expression() {
        return alf_expression;
    }

    public void setAlf_expression(alf_Expression alf_expression) {
        this.alf_expression = alf_expression;
    }
    public alf_Test getAlf_test() {
        return alf_test;
    }

    public void setAlf_test(alf_Test alf_test) {
        this.alf_test = alf_test;
    }

}
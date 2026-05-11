





import java.util.List;
import java.util.ArrayList;

public class SPL_OperatorExp extends Expression {

    private String opName;





    private SPL_Expression spl_expression;




    private SPL_Expression spl_expression;


    public SPL_OperatorExp(
        String opName    ) {
        super(
        );
        this.opName = opName;
    }


    public String getOpname() {
        return opName;
    }

    public void setOpname(String opName) {
        this.opName = opName;
    }

    public SPL_Expression getSpl_expression() {
        return spl_expression;
    }

    public void setSpl_expression(SPL_Expression spl_expression) {
        this.spl_expression = spl_expression;
    }
    public SPL_Expression getSpl_expression() {
        return spl_expression;
    }

    public void setSpl_expression(SPL_Expression spl_expression) {
        this.spl_expression = spl_expression;
    }

}
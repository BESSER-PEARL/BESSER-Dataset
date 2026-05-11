





import java.util.List;
import java.util.ArrayList;

public class dbl_ActivateObject extends SimpleStatement {

    private int priority;





    private dbl_Expression dbl_expression;


    public dbl_ActivateObject(
        int priority    ) {
        super(
        );
        this.priority = priority;
    }


    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }

    public dbl_Expression getDbl_expression() {
        return dbl_expression;
    }

    public void setDbl_expression(dbl_Expression dbl_expression) {
        this.dbl_expression = dbl_expression;
    }

}
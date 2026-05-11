





import java.util.List;
import java.util.ArrayList;

public class odemcustom_ActivateObject extends SimpleStatement {

    private int priority;





    private odemcustom_Expression odemcustom_expression;


    public odemcustom_ActivateObject(
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

    public odemcustom_Expression getOdemcustom_expression() {
        return odemcustom_expression;
    }

    public void setOdemcustom_expression(odemcustom_Expression odemcustom_expression) {
        this.odemcustom_expression = odemcustom_expression;
    }

}






import java.util.List;
import java.util.ArrayList;

public class oogen_OOTwoOperandAssignableExpression extends OOTwoOperandArithmeticExpression {

    private boolean assigned;



    public oogen_OOTwoOperandAssignableExpression(
        boolean assigned    ) {
        super(
        );
        this.assigned = assigned;
    }


    public boolean getAssigned() {
        return assigned;
    }

    public void setAssigned(boolean assigned) {
        this.assigned = assigned;
    }


}
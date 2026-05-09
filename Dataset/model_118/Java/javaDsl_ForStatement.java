





import java.util.List;
import java.util.ArrayList;

public class javaDsl_ForStatement extends Statement {

    private boolean condition;



    public javaDsl_ForStatement(
        boolean condition    ) {
        super(
        );
        this.condition = condition;
    }


    public boolean getCondition() {
        return condition;
    }

    public void setCondition(boolean condition) {
        this.condition = condition;
    }


}
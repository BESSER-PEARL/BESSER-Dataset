





import java.util.List;
import java.util.ArrayList;

public class project_LogicalBooleanLiteral extends LogicalExpression {

    private boolean isTrue;



    public project_LogicalBooleanLiteral(
        boolean isTrue    ) {
        super(
        );
        this.isTrue = isTrue;
    }


    public boolean getIstrue() {
        return isTrue;
    }

    public void setIstrue(boolean isTrue) {
        this.isTrue = isTrue;
    }


}
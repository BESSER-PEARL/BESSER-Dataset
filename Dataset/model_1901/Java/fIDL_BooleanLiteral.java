





import java.util.List;
import java.util.ArrayList;

public class fIDL_BooleanLiteral extends Expression {

    private boolean isTrue;



    public fIDL_BooleanLiteral(
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
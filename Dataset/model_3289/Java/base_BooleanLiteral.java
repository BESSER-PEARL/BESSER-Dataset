





import java.util.List;
import java.util.ArrayList;

public class base_BooleanLiteral extends Literal {

    private boolean isTrue;



    public base_BooleanLiteral(
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
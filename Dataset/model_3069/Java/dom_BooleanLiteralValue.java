





import java.util.List;
import java.util.ArrayList;

public class dom_BooleanLiteralValue extends LiteralValue {

    private boolean isTrue;



    public dom_BooleanLiteralValue(
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
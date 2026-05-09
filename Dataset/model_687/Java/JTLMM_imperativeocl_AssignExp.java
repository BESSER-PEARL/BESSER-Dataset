





import java.util.List;
import java.util.ArrayList;

public class JTLMM_imperativeocl_AssignExp extends ImperativeExpression {

    private boolean isReset;



    public JTLMM_imperativeocl_AssignExp(
        boolean isReset    ) {
        super(
        );
        this.isReset = isReset;
    }


    public boolean getIsreset() {
        return isReset;
    }

    public void setIsreset(boolean isReset) {
        this.isReset = isReset;
    }


}
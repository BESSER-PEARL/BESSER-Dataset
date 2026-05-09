





import java.util.List;
import java.util.ArrayList;

public class imperativeocl_AssignExp extends ImperativeExpression {

    private String isReset;



    public imperativeocl_AssignExp(
        String isReset    ) {
        super(
        );
        this.isReset = isReset;
    }


    public String getIsreset() {
        return isReset;
    }

    public void setIsreset(String isReset) {
        this.isReset = isReset;
    }


}
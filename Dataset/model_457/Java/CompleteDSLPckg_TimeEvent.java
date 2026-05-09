





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_TimeEvent  {

    private boolean isRelative;





    private CompleteDSLPckg_TimeExpression completedslpckg_timeexpression;


    public CompleteDSLPckg_TimeEvent(
        boolean isRelative    ) {
        this.isRelative = isRelative;
    }


    public boolean getIsrelative() {
        return isRelative;
    }

    public void setIsrelative(boolean isRelative) {
        this.isRelative = isRelative;
    }

    public CompleteDSLPckg_TimeExpression getCompletedslpckg_timeexpression() {
        return completedslpckg_timeexpression;
    }

    public void setCompletedslpckg_timeexpression(CompleteDSLPckg_TimeExpression completedslpckg_timeexpression) {
        this.completedslpckg_timeexpression = completedslpckg_timeexpression;
    }

}
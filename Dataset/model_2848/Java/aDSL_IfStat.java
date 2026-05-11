





import java.util.List;
import java.util.ArrayList;

public class aDSL_IfStat extends Statement {

    private boolean iselse;



    public aDSL_IfStat(
        boolean iselse    ) {
        super(
        );
        this.iselse = iselse;
    }


    public boolean getIselse() {
        return iselse;
    }

    public void setIselse(boolean iselse) {
        this.iselse = iselse;
    }


}
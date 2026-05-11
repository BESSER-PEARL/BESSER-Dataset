





import java.util.List;
import java.util.ArrayList;

public class nuSMV_RangeExpression  {

    private String lower;
    private String upper;



    public nuSMV_RangeExpression(
        String lower,        String upper    ) {
        this.lower = lower;
        this.upper = upper;
    }


    public String getLower() {
        return lower;
    }

    public void setLower(String lower) {
        this.lower = lower;
    }
    public String getUpper() {
        return upper;
    }

    public void setUpper(String upper) {
        this.upper = upper;
    }


}
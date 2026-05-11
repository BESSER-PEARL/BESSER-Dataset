





import java.util.List;
import java.util.ArrayList;

public class robochart_RangeExp extends Expression {

    private String linterval;
    private String rinterval;



    public robochart_RangeExp(
        String linterval,        String rinterval    ) {
        super(
        );
        this.linterval = linterval;
        this.rinterval = rinterval;
    }


    public String getLinterval() {
        return linterval;
    }

    public void setLinterval(String linterval) {
        this.linterval = linterval;
    }
    public String getRinterval() {
        return rinterval;
    }

    public void setRinterval(String rinterval) {
        this.rinterval = rinterval;
    }


}






import java.util.List;
import java.util.ArrayList;

public class robochart_RangeExp extends Expression {

    private String rinterval;
    private String linterval;



    public robochart_RangeExp(
        String rinterval,        String linterval    ) {
        super(
        );
        this.rinterval = rinterval;
        this.linterval = linterval;
    }


    public String getRinterval() {
        return rinterval;
    }

    public void setRinterval(String rinterval) {
        this.rinterval = rinterval;
    }
    public String getLinterval() {
        return linterval;
    }

    public void setLinterval(String linterval) {
        this.linterval = linterval;
    }


}
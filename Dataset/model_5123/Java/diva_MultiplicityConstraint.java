





import java.util.List;
import java.util.ArrayList;

public class diva_MultiplicityConstraint extends Constraint {

    private String lower;
    private String upper;



    public diva_MultiplicityConstraint(
        String lower,        String upper    ) {
        super(
        );
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
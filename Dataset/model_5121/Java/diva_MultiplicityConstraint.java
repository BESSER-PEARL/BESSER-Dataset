





import java.util.List;
import java.util.ArrayList;

public class diva_MultiplicityConstraint extends Constraint {

    private String upper;
    private String lower;





    private diva_Dimension diva_dimension;


    public diva_MultiplicityConstraint(
        String upper,        String lower    ) {
        super(
        );
        this.upper = upper;
        this.lower = lower;
    }


    public String getUpper() {
        return upper;
    }

    public void setUpper(String upper) {
        this.upper = upper;
    }
    public String getLower() {
        return lower;
    }

    public void setLower(String lower) {
        this.lower = lower;
    }

    public diva_Dimension getDiva_dimension() {
        return diva_dimension;
    }

    public void setDiva_dimension(diva_Dimension diva_dimension) {
        this.diva_dimension = diva_dimension;
    }

}
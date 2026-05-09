





import java.util.List;
import java.util.ArrayList;

public class rapidml_RegExConstraint extends Constraint {

    private String pattern;



    public rapidml_RegExConstraint(
        String pattern    ) {
        super(
        );
        this.pattern = pattern;
    }


    public String getPattern() {
        return pattern;
    }

    public void setPattern(String pattern) {
        this.pattern = pattern;
    }


}
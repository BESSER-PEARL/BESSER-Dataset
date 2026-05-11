





import java.util.List;
import java.util.ArrayList;

public class model_AbstractRegExpConstraint extends AbstractConstraint {

    private String regexp;



    public model_AbstractRegExpConstraint(
        String regexp    ) {
        super(
        );
        this.regexp = regexp;
    }


    public String getRegexp() {
        return regexp;
    }

    public void setRegexp(String regexp) {
        this.regexp = regexp;
    }


}
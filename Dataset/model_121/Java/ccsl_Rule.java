





import java.util.List;
import java.util.ArrayList;

public class ccsl_Rule extends Root {

    private String negated;



    public ccsl_Rule(
        String negated    ) {
        super(
        );
        this.negated = negated;
    }


    public String getNegated() {
        return negated;
    }

    public void setNegated(String negated) {
        this.negated = negated;
    }


}
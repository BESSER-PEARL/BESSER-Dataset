





import java.util.List;
import java.util.ArrayList;

public class ccsl_filters_Filter extends CcslBooleanFunction {

    private String negated;



    public ccsl_filters_Filter(
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
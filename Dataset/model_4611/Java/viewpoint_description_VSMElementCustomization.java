





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_VSMElementCustomization extends IVSMElementCustomization {

    private String predicateExpression;



    public viewpoint_description_VSMElementCustomization(
        String predicateExpression    ) {
        super(
        );
        this.predicateExpression = predicateExpression;
    }


    public String getPredicateexpression() {
        return predicateExpression;
    }

    public void setPredicateexpression(String predicateExpression) {
        this.predicateExpression = predicateExpression;
    }


}
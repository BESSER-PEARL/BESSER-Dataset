





import java.util.List;
import java.util.ArrayList;

public class vql_CompareConstraint extends Constraint {

    private String feature;



    public vql_CompareConstraint(
        String feature    ) {
        super(
        );
        this.feature = feature;
    }


    public String getFeature() {
        return feature;
    }

    public void setFeature(String feature) {
        this.feature = feature;
    }


}
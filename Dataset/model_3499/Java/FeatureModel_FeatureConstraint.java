





import java.util.List;
import java.util.ArrayList;

public class FeatureModel_FeatureConstraint extends Constraint {

    private String type;



    public FeatureModel_FeatureConstraint(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}
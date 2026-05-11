





import java.util.List;
import java.util.ArrayList;

public class aredsl_UnsetOperation extends DomainOperation {

    private String constraint;
    private String feature;



    public aredsl_UnsetOperation(
        String constraint,        String feature    ) {
        super(
        );
        this.constraint = constraint;
        this.feature = feature;
    }


    public String getConstraint() {
        return constraint;
    }

    public void setConstraint(String constraint) {
        this.constraint = constraint;
    }
    public String getFeature() {
        return feature;
    }

    public void setFeature(String feature) {
        this.feature = feature;
    }


}
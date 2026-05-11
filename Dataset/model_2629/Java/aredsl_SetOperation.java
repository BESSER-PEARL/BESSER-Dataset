





import java.util.List;
import java.util.ArrayList;

public class aredsl_SetOperation extends DomainOperation {

    private String constraint;
    private String value;
    private String feature;



    public aredsl_SetOperation(
        String constraint,        String value,        String feature    ) {
        super(
        );
        this.constraint = constraint;
        this.value = value;
        this.feature = feature;
    }


    public String getConstraint() {
        return constraint;
    }

    public void setConstraint(String constraint) {
        this.constraint = constraint;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getFeature() {
        return feature;
    }

    public void setFeature(String feature) {
        this.feature = feature;
    }


}
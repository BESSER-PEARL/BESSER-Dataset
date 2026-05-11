





import java.util.List;
import java.util.ArrayList;

public class viewpoint_validation_SemanticValidationRule extends ValidationRule {

    private String targetClass;



    public viewpoint_validation_SemanticValidationRule(
        String targetClass    ) {
        super(
        );
        this.targetClass = targetClass;
    }


    public String getTargetclass() {
        return targetClass;
    }

    public void setTargetclass(String targetClass) {
        this.targetClass = targetClass;
    }


}
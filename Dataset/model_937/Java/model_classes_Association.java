





import java.util.List;
import java.util.ArrayList;

public class model_classes_Association extends UnicaseModelElement {

    private String sourceMultiplicity;
    private String type;
    private String targetRole;
    private String sourceRole;
    private String targetMultiplicity;



    public model_classes_Association(
        String sourceMultiplicity,        String type,        String targetRole,        String sourceRole,        String targetMultiplicity    ) {
        super(
        );
        this.sourceMultiplicity = sourceMultiplicity;
        this.type = type;
        this.targetRole = targetRole;
        this.sourceRole = sourceRole;
        this.targetMultiplicity = targetMultiplicity;
    }


    public String getSourcemultiplicity() {
        return sourceMultiplicity;
    }

    public void setSourcemultiplicity(String sourceMultiplicity) {
        this.sourceMultiplicity = sourceMultiplicity;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getTargetrole() {
        return targetRole;
    }

    public void setTargetrole(String targetRole) {
        this.targetRole = targetRole;
    }
    public String getSourcerole() {
        return sourceRole;
    }

    public void setSourcerole(String sourceRole) {
        this.sourceRole = sourceRole;
    }
    public String getTargetmultiplicity() {
        return targetMultiplicity;
    }

    public void setTargetmultiplicity(String targetMultiplicity) {
        this.targetMultiplicity = targetMultiplicity;
    }


}
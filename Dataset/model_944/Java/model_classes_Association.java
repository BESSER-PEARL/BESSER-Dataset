





import java.util.List;
import java.util.ArrayList;

public class model_classes_Association extends UnicaseModelElement {

    private String targetMultiplicity;
    private String type;
    private String sourceRole;
    private String targetRole;
    private String sourceMultiplicity;



    public model_classes_Association(
        String targetMultiplicity,        String type,        String sourceRole,        String targetRole,        String sourceMultiplicity    ) {
        super(
        );
        this.targetMultiplicity = targetMultiplicity;
        this.type = type;
        this.sourceRole = sourceRole;
        this.targetRole = targetRole;
        this.sourceMultiplicity = sourceMultiplicity;
    }


    public String getTargetmultiplicity() {
        return targetMultiplicity;
    }

    public void setTargetmultiplicity(String targetMultiplicity) {
        this.targetMultiplicity = targetMultiplicity;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getSourcerole() {
        return sourceRole;
    }

    public void setSourcerole(String sourceRole) {
        this.sourceRole = sourceRole;
    }
    public String getTargetrole() {
        return targetRole;
    }

    public void setTargetrole(String targetRole) {
        this.targetRole = targetRole;
    }
    public String getSourcemultiplicity() {
        return sourceMultiplicity;
    }

    public void setSourcemultiplicity(String sourceMultiplicity) {
        this.sourceMultiplicity = sourceMultiplicity;
    }


}
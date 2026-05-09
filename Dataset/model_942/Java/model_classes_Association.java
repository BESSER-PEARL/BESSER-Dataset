





import java.util.List;
import java.util.ArrayList;

public class model_classes_Association extends UnicaseModelElement {

    private String sourceMultiplicity;
    private String type;
    private String targetMultiplicity;
    private String targetRole;
    private String sourceRole;



    public model_classes_Association(
        String sourceMultiplicity,        String type,        String targetMultiplicity,        String targetRole,        String sourceRole    ) {
        super(
        );
        this.sourceMultiplicity = sourceMultiplicity;
        this.type = type;
        this.targetMultiplicity = targetMultiplicity;
        this.targetRole = targetRole;
        this.sourceRole = sourceRole;
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
    public String getTargetmultiplicity() {
        return targetMultiplicity;
    }

    public void setTargetmultiplicity(String targetMultiplicity) {
        this.targetMultiplicity = targetMultiplicity;
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


}






import java.util.List;
import java.util.ArrayList;

public class yuml_Association extends Relationship {

    private boolean navigableTarget;
    private boolean navigableSource;
    private String sourceVisibility;
    private String targetVisibility;
    private String type;



    public yuml_Association(
        boolean navigableTarget,        boolean navigableSource,        String sourceVisibility,        String targetVisibility,        String type    ) {
        super(
        );
        this.navigableTarget = navigableTarget;
        this.navigableSource = navigableSource;
        this.sourceVisibility = sourceVisibility;
        this.targetVisibility = targetVisibility;
        this.type = type;
    }


    public boolean getNavigabletarget() {
        return navigableTarget;
    }

    public void setNavigabletarget(boolean navigableTarget) {
        this.navigableTarget = navigableTarget;
    }
    public boolean getNavigablesource() {
        return navigableSource;
    }

    public void setNavigablesource(boolean navigableSource) {
        this.navigableSource = navigableSource;
    }
    public String getSourcevisibility() {
        return sourceVisibility;
    }

    public void setSourcevisibility(String sourceVisibility) {
        this.sourceVisibility = sourceVisibility;
    }
    public String getTargetvisibility() {
        return targetVisibility;
    }

    public void setTargetvisibility(String targetVisibility) {
        this.targetVisibility = targetVisibility;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}
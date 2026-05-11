





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_Viewpoint extends description_EndUserDocumentedElement, description_Component, description_IdentifiedElement, description_DocumentedElement {

    private String reuses;
    private String conflicts;
    private String icon;
    private String modelFileExtension;
    private String customizes;



    public viewpoint_description_Viewpoint(
        String reuses,        String conflicts,        String icon,        String modelFileExtension,        String customizes    ) {
        super(
        );
        this.reuses = reuses;
        this.conflicts = conflicts;
        this.icon = icon;
        this.modelFileExtension = modelFileExtension;
        this.customizes = customizes;
    }


    public String getReuses() {
        return reuses;
    }

    public void setReuses(String reuses) {
        this.reuses = reuses;
    }
    public String getConflicts() {
        return conflicts;
    }

    public void setConflicts(String conflicts) {
        this.conflicts = conflicts;
    }
    public String getIcon() {
        return icon;
    }

    public void setIcon(String icon) {
        this.icon = icon;
    }
    public String getModelfileextension() {
        return modelFileExtension;
    }

    public void setModelfileextension(String modelFileExtension) {
        this.modelFileExtension = modelFileExtension;
    }
    public String getCustomizes() {
        return customizes;
    }

    public void setCustomizes(String customizes) {
        this.customizes = customizes;
    }


}
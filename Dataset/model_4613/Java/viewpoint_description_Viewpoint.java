





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_Viewpoint extends description_EndUserDocumentedElement, description_DocumentedElement, description_Component, description_IdentifiedElement {

    private String modelFileExtension;
    private String customizes;
    private String icon;
    private String conflicts;
    private String reuses;





    private List<RepresentationDescription> representationdescriptions;


    public viewpoint_description_Viewpoint(
        String modelFileExtension,        String customizes,        String icon,        String conflicts,        String reuses    ) {
        super(
        );
        this.modelFileExtension = modelFileExtension;
        this.customizes = customizes;
        this.icon = icon;
        this.conflicts = conflicts;
        this.reuses = reuses;
        this.representationdescriptions = new ArrayList<>();
    }

    public viewpoint_description_Viewpoint(
        String modelFileExtension,        String customizes,        String icon,        String conflicts,        String reuses        ArrayList<RepresentationDescription> representationdescriptions    ) {
        this.modelFileExtension = modelFileExtension;
        this.customizes = customizes;
        this.icon = icon;
        this.conflicts = conflicts;
        this.reuses = reuses;
        this.representationdescriptions = representationdescriptions;
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
    public String getIcon() {
        return icon;
    }

    public void setIcon(String icon) {
        this.icon = icon;
    }
    public String getConflicts() {
        return conflicts;
    }

    public void setConflicts(String conflicts) {
        this.conflicts = conflicts;
    }
    public String getReuses() {
        return reuses;
    }

    public void setReuses(String reuses) {
        this.reuses = reuses;
    }

    public List<RepresentationDescription> getRepresentationdescriptions() {
        return representationdescriptions;
    }

    public void addRepresentationdescription(Representationdescription representationdescription) {
        this.representationdescriptions.add(representationdescription);
    }

}






import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_Viewpoint extends description_Component, description_IdentifiedElement, description_EndUserDocumentedElement, description_DocumentedElement {

    private String customizes;
    private String icon;
    private String conflicts;
    private String reuses;
    private String modelFileExtension;





    private List<FeatureExtensionDescription> featureextensiondescriptions;


    public viewpoint_description_Viewpoint(
        String customizes,        String icon,        String conflicts,        String reuses,        String modelFileExtension    ) {
        super(
        );
        this.customizes = customizes;
        this.icon = icon;
        this.conflicts = conflicts;
        this.reuses = reuses;
        this.modelFileExtension = modelFileExtension;
        this.featureextensiondescriptions = new ArrayList<>();
    }

    public viewpoint_description_Viewpoint(
        String customizes,        String icon,        String conflicts,        String reuses,        String modelFileExtension        ArrayList<FeatureExtensionDescription> featureextensiondescriptions    ) {
        this.customizes = customizes;
        this.icon = icon;
        this.conflicts = conflicts;
        this.reuses = reuses;
        this.modelFileExtension = modelFileExtension;
        this.featureextensiondescriptions = featureextensiondescriptions;
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
    public String getModelfileextension() {
        return modelFileExtension;
    }

    public void setModelfileextension(String modelFileExtension) {
        this.modelFileExtension = modelFileExtension;
    }

    public List<FeatureExtensionDescription> getFeatureextensiondescriptions() {
        return featureextensiondescriptions;
    }

    public void addFeatureextensiondescription(Featureextensiondescription featureextensiondescription) {
        this.featureextensiondescriptions.add(featureextensiondescription);
    }

}
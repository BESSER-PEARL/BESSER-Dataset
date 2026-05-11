





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_Viewpoint extends description_EndUserDocumentedElement, description_Component, description_DocumentedElement, description_IdentifiedElement {

    private String icon;
    private String modelFileExtension;
    private String reuses;
    private String conflicts;
    private String customizes;





    private List<FeatureExtensionDescription> featureextensiondescriptions;


    public viewpoint_description_Viewpoint(
        String icon,        String modelFileExtension,        String reuses,        String conflicts,        String customizes    ) {
        super(
        );
        this.icon = icon;
        this.modelFileExtension = modelFileExtension;
        this.reuses = reuses;
        this.conflicts = conflicts;
        this.customizes = customizes;
        this.featureextensiondescriptions = new ArrayList<>();
    }

    public viewpoint_description_Viewpoint(
        String icon,        String modelFileExtension,        String reuses,        String conflicts,        String customizes        ArrayList<FeatureExtensionDescription> featureextensiondescriptions    ) {
        this.icon = icon;
        this.modelFileExtension = modelFileExtension;
        this.reuses = reuses;
        this.conflicts = conflicts;
        this.customizes = customizes;
        this.featureextensiondescriptions = featureextensiondescriptions;
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
    public String getCustomizes() {
        return customizes;
    }

    public void setCustomizes(String customizes) {
        this.customizes = customizes;
    }

    public List<FeatureExtensionDescription> getFeatureextensiondescriptions() {
        return featureextensiondescriptions;
    }

    public void addFeatureextensiondescription(Featureextensiondescription featureextensiondescription) {
        this.featureextensiondescriptions.add(featureextensiondescription);
    }

}
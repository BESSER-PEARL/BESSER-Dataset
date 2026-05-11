





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_Viewpoint extends description_DocumentedElement, description_EndUserDocumentedElement, description_Component, description_IdentifiedElement {

    private String customizes;
    private String conflicts;
    private String modelFileExtension;
    private String reuses;
    private String icon;





    private List<FeatureExtensionDescription> featureextensiondescriptions;


    public viewpoint_description_Viewpoint(
        String customizes,        String conflicts,        String modelFileExtension,        String reuses,        String icon    ) {
        super(
        );
        this.customizes = customizes;
        this.conflicts = conflicts;
        this.modelFileExtension = modelFileExtension;
        this.reuses = reuses;
        this.icon = icon;
        this.featureextensiondescriptions = new ArrayList<>();
    }

    public viewpoint_description_Viewpoint(
        String customizes,        String conflicts,        String modelFileExtension,        String reuses,        String icon        ArrayList<FeatureExtensionDescription> featureextensiondescriptions    ) {
        this.customizes = customizes;
        this.conflicts = conflicts;
        this.modelFileExtension = modelFileExtension;
        this.reuses = reuses;
        this.icon = icon;
        this.featureextensiondescriptions = featureextensiondescriptions;
    }

    public String getCustomizes() {
        return customizes;
    }

    public void setCustomizes(String customizes) {
        this.customizes = customizes;
    }
    public String getConflicts() {
        return conflicts;
    }

    public void setConflicts(String conflicts) {
        this.conflicts = conflicts;
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
    public String getIcon() {
        return icon;
    }

    public void setIcon(String icon) {
        this.icon = icon;
    }

    public List<FeatureExtensionDescription> getFeatureextensiondescriptions() {
        return featureextensiondescriptions;
    }

    public void addFeatureextensiondescription(Featureextensiondescription featureextensiondescription) {
        this.featureextensiondescriptions.add(featureextensiondescription);
    }

}
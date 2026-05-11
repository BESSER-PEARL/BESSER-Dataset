





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_Viewpoint extends description_DocumentedElement, description_Component, description_IdentifiedElement, description_EndUserDocumentedElement {

    private String conflicts;
    private String customizes;
    private String icon;
    private String modelFileExtension;
    private String reuses;





    private List<FeatureExtensionDescription> featureextensiondescriptions;


    public viewpoint_description_Viewpoint(
        String conflicts,        String customizes,        String icon,        String modelFileExtension,        String reuses    ) {
        super(
        );
        this.conflicts = conflicts;
        this.customizes = customizes;
        this.icon = icon;
        this.modelFileExtension = modelFileExtension;
        this.reuses = reuses;
        this.featureextensiondescriptions = new ArrayList<>();
    }

    public viewpoint_description_Viewpoint(
        String conflicts,        String customizes,        String icon,        String modelFileExtension,        String reuses        ArrayList<FeatureExtensionDescription> featureextensiondescriptions    ) {
        this.conflicts = conflicts;
        this.customizes = customizes;
        this.icon = icon;
        this.modelFileExtension = modelFileExtension;
        this.reuses = reuses;
        this.featureextensiondescriptions = featureextensiondescriptions;
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

    public List<FeatureExtensionDescription> getFeatureextensiondescriptions() {
        return featureextensiondescriptions;
    }

    public void addFeatureextensiondescription(Featureextensiondescription featureextensiondescription) {
        this.featureextensiondescriptions.add(featureextensiondescription);
    }

}






import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_Viewpoint extends description_Component, description_EndUserDocumentedElement, description_IdentifiedElement, description_DocumentedElement {

    private String conflicts;
    private String customizes;
    private String modelFileExtension;
    private String reuses;
    private String icon;





    private List<RepresentationDescription> representationdescriptions;




    private List<FeatureExtensionDescription> featureextensiondescriptions;


    public viewpoint_description_Viewpoint(
        String conflicts,        String customizes,        String modelFileExtension,        String reuses,        String icon    ) {
        super(
        );
        this.conflicts = conflicts;
        this.customizes = customizes;
        this.modelFileExtension = modelFileExtension;
        this.reuses = reuses;
        this.icon = icon;
        this.representationdescriptions = new ArrayList<>();
        this.featureextensiondescriptions = new ArrayList<>();
    }

    public viewpoint_description_Viewpoint(
        String conflicts,        String customizes,        String modelFileExtension,        String reuses,        String icon        ArrayList<RepresentationDescription> representationdescriptions,        ArrayList<FeatureExtensionDescription> featureextensiondescriptions    ) {
        this.conflicts = conflicts;
        this.customizes = customizes;
        this.modelFileExtension = modelFileExtension;
        this.reuses = reuses;
        this.icon = icon;
        this.representationdescriptions = representationdescriptions;
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

    public List<RepresentationDescription> getRepresentationdescriptions() {
        return representationdescriptions;
    }

    public void addRepresentationdescription(Representationdescription representationdescription) {
        this.representationdescriptions.add(representationdescription);
    }
    public List<FeatureExtensionDescription> getFeatureextensiondescriptions() {
        return featureextensiondescriptions;
    }

    public void addFeatureextensiondescription(Featureextensiondescription featureextensiondescription) {
        this.featureextensiondescriptions.add(featureextensiondescription);
    }

}






import java.util.List;
import java.util.ArrayList;

public class servicefeaturemodel_ServiceFeature  {

    private String id;
    private String description;
    private boolean mapsToGSMElement;
    private int maxAmount;
    private int minAmount;
    private String featureType;
    private String name;
    private boolean required;
    private String associatedGSMElement;





    private servicefeaturemodel_ServiceFeatureDiagram servicefeaturemodel_servicefeaturediagram;




    private List<servicefeaturemodel_Requires> servicefeaturemodel_requiress;




    private servicefeaturemodel_Excludes servicefeaturemodel_excludes;




    private List<servicefeaturemodel_ServiceFeature> servicefeaturemodel_servicefeatures;




    private servicefeaturemodel_Requires servicefeaturemodel_requires;




    private servicefeaturemodel_Variant servicefeaturemodel_variant;




    private List<servicefeaturemodel_Excludes> servicefeaturemodel_excludess;




    private List<servicefeaturemodel_Attribute> servicefeaturemodel_attributes;


    public servicefeaturemodel_ServiceFeature(
        String id,        String description,        boolean mapsToGSMElement,        int maxAmount,        int minAmount,        String featureType,        String name,        boolean required,        String associatedGSMElement    ) {
        this.id = id;
        this.description = description;
        this.mapsToGSMElement = mapsToGSMElement;
        this.maxAmount = maxAmount;
        this.minAmount = minAmount;
        this.featureType = featureType;
        this.name = name;
        this.required = required;
        this.associatedGSMElement = associatedGSMElement;
        this.servicefeaturemodel_requiress = new ArrayList<>();
        this.servicefeaturemodel_servicefeatures = new ArrayList<>();
        this.servicefeaturemodel_excludess = new ArrayList<>();
        this.servicefeaturemodel_attributes = new ArrayList<>();
    }

    public servicefeaturemodel_ServiceFeature(
        String id,        String description,        boolean mapsToGSMElement,        int maxAmount,        int minAmount,        String featureType,        String name,        boolean required,        String associatedGSMElement        ArrayList<servicefeaturemodel_Requires> servicefeaturemodel_requiress,        ArrayList<servicefeaturemodel_ServiceFeature> servicefeaturemodel_servicefeatures,        ArrayList<servicefeaturemodel_Excludes> servicefeaturemodel_excludess,        ArrayList<servicefeaturemodel_Attribute> servicefeaturemodel_attributes    ) {
        this.id = id;
        this.description = description;
        this.mapsToGSMElement = mapsToGSMElement;
        this.maxAmount = maxAmount;
        this.minAmount = minAmount;
        this.featureType = featureType;
        this.name = name;
        this.required = required;
        this.associatedGSMElement = associatedGSMElement;
        this.servicefeaturemodel_requiress = servicefeaturemodel_requiress;
        this.servicefeaturemodel_servicefeatures = servicefeaturemodel_servicefeatures;
        this.servicefeaturemodel_excludess = servicefeaturemodel_excludess;
        this.servicefeaturemodel_attributes = servicefeaturemodel_attributes;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public boolean getMapstogsmelement() {
        return mapsToGSMElement;
    }

    public void setMapstogsmelement(boolean mapsToGSMElement) {
        this.mapsToGSMElement = mapsToGSMElement;
    }
    public int getMaxamount() {
        return maxAmount;
    }

    public void setMaxamount(int maxAmount) {
        this.maxAmount = maxAmount;
    }
    public int getMinamount() {
        return minAmount;
    }

    public void setMinamount(int minAmount) {
        this.minAmount = minAmount;
    }
    public String getFeaturetype() {
        return featureType;
    }

    public void setFeaturetype(String featureType) {
        this.featureType = featureType;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getRequired() {
        return required;
    }

    public void setRequired(boolean required) {
        this.required = required;
    }
    public String getAssociatedgsmelement() {
        return associatedGSMElement;
    }

    public void setAssociatedgsmelement(String associatedGSMElement) {
        this.associatedGSMElement = associatedGSMElement;
    }

    public servicefeaturemodel_ServiceFeatureDiagram getServicefeaturemodel_servicefeaturediagram() {
        return servicefeaturemodel_servicefeaturediagram;
    }

    public void setServicefeaturemodel_servicefeaturediagram(servicefeaturemodel_ServiceFeatureDiagram servicefeaturemodel_servicefeaturediagram) {
        this.servicefeaturemodel_servicefeaturediagram = servicefeaturemodel_servicefeaturediagram;
    }
    public List<servicefeaturemodel_Requires> getServicefeaturemodel_requiress() {
        return servicefeaturemodel_requiress;
    }

    public void addServicefeaturemodel_requires(Servicefeaturemodel_requires servicefeaturemodel_requires) {
        this.servicefeaturemodel_requiress.add(servicefeaturemodel_requires);
    }
    public servicefeaturemodel_Excludes getServicefeaturemodel_excludes() {
        return servicefeaturemodel_excludes;
    }

    public void setServicefeaturemodel_excludes(servicefeaturemodel_Excludes servicefeaturemodel_excludes) {
        this.servicefeaturemodel_excludes = servicefeaturemodel_excludes;
    }
    public List<servicefeaturemodel_ServiceFeature> getServicefeaturemodel_servicefeatures() {
        return servicefeaturemodel_servicefeatures;
    }

    public void addServicefeaturemodel_servicefeature(Servicefeaturemodel_servicefeature servicefeaturemodel_servicefeature) {
        this.servicefeaturemodel_servicefeatures.add(servicefeaturemodel_servicefeature);
    }
    public servicefeaturemodel_Requires getServicefeaturemodel_requires() {
        return servicefeaturemodel_requires;
    }

    public void setServicefeaturemodel_requires(servicefeaturemodel_Requires servicefeaturemodel_requires) {
        this.servicefeaturemodel_requires = servicefeaturemodel_requires;
    }
    public servicefeaturemodel_Variant getServicefeaturemodel_variant() {
        return servicefeaturemodel_variant;
    }

    public void setServicefeaturemodel_variant(servicefeaturemodel_Variant servicefeaturemodel_variant) {
        this.servicefeaturemodel_variant = servicefeaturemodel_variant;
    }
    public List<servicefeaturemodel_Excludes> getServicefeaturemodel_excludess() {
        return servicefeaturemodel_excludess;
    }

    public void addServicefeaturemodel_excludes(Servicefeaturemodel_excludes servicefeaturemodel_excludes) {
        this.servicefeaturemodel_excludess.add(servicefeaturemodel_excludes);
    }
    public List<servicefeaturemodel_Attribute> getServicefeaturemodel_attributes() {
        return servicefeaturemodel_attributes;
    }

    public void addServicefeaturemodel_attribute(Servicefeaturemodel_attribute servicefeaturemodel_attribute) {
        this.servicefeaturemodel_attributes.add(servicefeaturemodel_attribute);
    }

}
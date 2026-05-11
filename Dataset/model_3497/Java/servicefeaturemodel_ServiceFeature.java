





import java.util.List;
import java.util.ArrayList;

public class servicefeaturemodel_ServiceFeature  {

    private boolean mapsToGSMElement;
    private int maxAmount;
    private String description;
    private String name;
    private String associatedGSMElement;
    private String id;
    private int minAmount;
    private boolean required;
    private String featureType;





    private servicefeaturemodel_ServiceFeature servicefeaturemodel_servicefeature;




    private servicefeaturemodel_ServiceFeatureDiagram servicefeaturemodel_servicefeaturediagram;


    public servicefeaturemodel_ServiceFeature(
        boolean mapsToGSMElement,        int maxAmount,        String description,        String name,        String associatedGSMElement,        String id,        int minAmount,        boolean required,        String featureType    ) {
        this.mapsToGSMElement = mapsToGSMElement;
        this.maxAmount = maxAmount;
        this.description = description;
        this.name = name;
        this.associatedGSMElement = associatedGSMElement;
        this.id = id;
        this.minAmount = minAmount;
        this.required = required;
        this.featureType = featureType;
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
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAssociatedgsmelement() {
        return associatedGSMElement;
    }

    public void setAssociatedgsmelement(String associatedGSMElement) {
        this.associatedGSMElement = associatedGSMElement;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public int getMinamount() {
        return minAmount;
    }

    public void setMinamount(int minAmount) {
        this.minAmount = minAmount;
    }
    public boolean getRequired() {
        return required;
    }

    public void setRequired(boolean required) {
        this.required = required;
    }
    public String getFeaturetype() {
        return featureType;
    }

    public void setFeaturetype(String featureType) {
        this.featureType = featureType;
    }

    public servicefeaturemodel_ServiceFeature getServicefeaturemodel_servicefeature() {
        return servicefeaturemodel_servicefeature;
    }

    public void setServicefeaturemodel_servicefeature(servicefeaturemodel_ServiceFeature servicefeaturemodel_servicefeature) {
        this.servicefeaturemodel_servicefeature = servicefeaturemodel_servicefeature;
    }
    public servicefeaturemodel_ServiceFeatureDiagram getServicefeaturemodel_servicefeaturediagram() {
        return servicefeaturemodel_servicefeaturediagram;
    }

    public void setServicefeaturemodel_servicefeaturediagram(servicefeaturemodel_ServiceFeatureDiagram servicefeaturemodel_servicefeaturediagram) {
        this.servicefeaturemodel_servicefeaturediagram = servicefeaturemodel_servicefeaturediagram;
    }

}
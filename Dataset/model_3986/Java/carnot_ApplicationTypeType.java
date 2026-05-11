





import java.util.List;
import java.util.ArrayList;

public class carnot_ApplicationTypeType extends IMetaType {

    private String instanceClass;
    private String accessPointProviderClass;
    private String panelClass;
    private String validatorClass;
    private String synchronous;





    private List<carnot_ApplicationType> carnot_applicationtypes;




    private carnot_ModelType carnot_modeltype;




    private carnot_ApplicationType carnot_applicationtype;


    public carnot_ApplicationTypeType(
        String instanceClass,        String accessPointProviderClass,        String panelClass,        String validatorClass,        String synchronous    ) {
        super(
        );
        this.instanceClass = instanceClass;
        this.accessPointProviderClass = accessPointProviderClass;
        this.panelClass = panelClass;
        this.validatorClass = validatorClass;
        this.synchronous = synchronous;
        this.carnot_applicationtypes = new ArrayList<>();
    }

    public carnot_ApplicationTypeType(
        String instanceClass,        String accessPointProviderClass,        String panelClass,        String validatorClass,        String synchronous        ArrayList<carnot_ApplicationType> carnot_applicationtypes    ) {
        this.instanceClass = instanceClass;
        this.accessPointProviderClass = accessPointProviderClass;
        this.panelClass = panelClass;
        this.validatorClass = validatorClass;
        this.synchronous = synchronous;
        this.carnot_applicationtypes = carnot_applicationtypes;
    }

    public String getInstanceclass() {
        return instanceClass;
    }

    public void setInstanceclass(String instanceClass) {
        this.instanceClass = instanceClass;
    }
    public String getAccesspointproviderclass() {
        return accessPointProviderClass;
    }

    public void setAccesspointproviderclass(String accessPointProviderClass) {
        this.accessPointProviderClass = accessPointProviderClass;
    }
    public String getPanelclass() {
        return panelClass;
    }

    public void setPanelclass(String panelClass) {
        this.panelClass = panelClass;
    }
    public String getValidatorclass() {
        return validatorClass;
    }

    public void setValidatorclass(String validatorClass) {
        this.validatorClass = validatorClass;
    }
    public String getSynchronous() {
        return synchronous;
    }

    public void setSynchronous(String synchronous) {
        this.synchronous = synchronous;
    }

    public List<carnot_ApplicationType> getCarnot_applicationtypes() {
        return carnot_applicationtypes;
    }

    public void addCarnot_applicationtype(Carnot_applicationtype carnot_applicationtype) {
        this.carnot_applicationtypes.add(carnot_applicationtype);
    }
    public carnot_ModelType getCarnot_modeltype() {
        return carnot_modeltype;
    }

    public void setCarnot_modeltype(carnot_ModelType carnot_modeltype) {
        this.carnot_modeltype = carnot_modeltype;
    }
    public carnot_ApplicationType getCarnot_applicationtype() {
        return carnot_applicationtype;
    }

    public void setCarnot_applicationtype(carnot_ApplicationType carnot_applicationtype) {
        this.carnot_applicationtype = carnot_applicationtype;
    }

}
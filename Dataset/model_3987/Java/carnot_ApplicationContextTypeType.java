





import java.util.List;
import java.util.ArrayList;

public class carnot_ApplicationContextTypeType extends IMetaType {

    private String validatorClass;
    private String accessPointProviderClass;
    private String hasMappingId;
    private String panelClass;
    private String hasApplicationPath;





    private List<carnot_ContextType> carnot_contexttypes;




    private carnot_ContextType carnot_contexttype;




    private carnot_ModelType carnot_modeltype;


    public carnot_ApplicationContextTypeType(
        String validatorClass,        String accessPointProviderClass,        String hasMappingId,        String panelClass,        String hasApplicationPath    ) {
        super(
        );
        this.validatorClass = validatorClass;
        this.accessPointProviderClass = accessPointProviderClass;
        this.hasMappingId = hasMappingId;
        this.panelClass = panelClass;
        this.hasApplicationPath = hasApplicationPath;
        this.carnot_contexttypes = new ArrayList<>();
    }

    public carnot_ApplicationContextTypeType(
        String validatorClass,        String accessPointProviderClass,        String hasMappingId,        String panelClass,        String hasApplicationPath        ArrayList<carnot_ContextType> carnot_contexttypes    ) {
        this.validatorClass = validatorClass;
        this.accessPointProviderClass = accessPointProviderClass;
        this.hasMappingId = hasMappingId;
        this.panelClass = panelClass;
        this.hasApplicationPath = hasApplicationPath;
        this.carnot_contexttypes = carnot_contexttypes;
    }

    public String getValidatorclass() {
        return validatorClass;
    }

    public void setValidatorclass(String validatorClass) {
        this.validatorClass = validatorClass;
    }
    public String getAccesspointproviderclass() {
        return accessPointProviderClass;
    }

    public void setAccesspointproviderclass(String accessPointProviderClass) {
        this.accessPointProviderClass = accessPointProviderClass;
    }
    public String getHasmappingid() {
        return hasMappingId;
    }

    public void setHasmappingid(String hasMappingId) {
        this.hasMappingId = hasMappingId;
    }
    public String getPanelclass() {
        return panelClass;
    }

    public void setPanelclass(String panelClass) {
        this.panelClass = panelClass;
    }
    public String getHasapplicationpath() {
        return hasApplicationPath;
    }

    public void setHasapplicationpath(String hasApplicationPath) {
        this.hasApplicationPath = hasApplicationPath;
    }

    public List<carnot_ContextType> getCarnot_contexttypes() {
        return carnot_contexttypes;
    }

    public void addCarnot_contexttype(Carnot_contexttype carnot_contexttype) {
        this.carnot_contexttypes.add(carnot_contexttype);
    }
    public carnot_ContextType getCarnot_contexttype() {
        return carnot_contexttype;
    }

    public void setCarnot_contexttype(carnot_ContextType carnot_contexttype) {
        this.carnot_contexttype = carnot_contexttype;
    }
    public carnot_ModelType getCarnot_modeltype() {
        return carnot_modeltype;
    }

    public void setCarnot_modeltype(carnot_ModelType carnot_modeltype) {
        this.carnot_modeltype = carnot_modeltype;
    }

}
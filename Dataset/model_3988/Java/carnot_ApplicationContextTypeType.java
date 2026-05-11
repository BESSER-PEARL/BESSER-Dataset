





import java.util.List;
import java.util.ArrayList;

public class carnot_ApplicationContextTypeType extends IMetaType {

    private String validatorClass;
    private String hasApplicationPath;
    private String accessPointProviderClass;
    private String panelClass;
    private String hasMappingId;





    private carnot_ModelType carnot_modeltype;




    private carnot_ContextType carnot_contexttype;




    private List<carnot_ContextType> carnot_contexttypes;


    public carnot_ApplicationContextTypeType(
        String validatorClass,        String hasApplicationPath,        String accessPointProviderClass,        String panelClass,        String hasMappingId    ) {
        super(
        );
        this.validatorClass = validatorClass;
        this.hasApplicationPath = hasApplicationPath;
        this.accessPointProviderClass = accessPointProviderClass;
        this.panelClass = panelClass;
        this.hasMappingId = hasMappingId;
        this.carnot_contexttypes = new ArrayList<>();
    }

    public carnot_ApplicationContextTypeType(
        String validatorClass,        String hasApplicationPath,        String accessPointProviderClass,        String panelClass,        String hasMappingId        ArrayList<carnot_ContextType> carnot_contexttypes    ) {
        this.validatorClass = validatorClass;
        this.hasApplicationPath = hasApplicationPath;
        this.accessPointProviderClass = accessPointProviderClass;
        this.panelClass = panelClass;
        this.hasMappingId = hasMappingId;
        this.carnot_contexttypes = carnot_contexttypes;
    }

    public String getValidatorclass() {
        return validatorClass;
    }

    public void setValidatorclass(String validatorClass) {
        this.validatorClass = validatorClass;
    }
    public String getHasapplicationpath() {
        return hasApplicationPath;
    }

    public void setHasapplicationpath(String hasApplicationPath) {
        this.hasApplicationPath = hasApplicationPath;
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
    public String getHasmappingid() {
        return hasMappingId;
    }

    public void setHasmappingid(String hasMappingId) {
        this.hasMappingId = hasMappingId;
    }

    public carnot_ModelType getCarnot_modeltype() {
        return carnot_modeltype;
    }

    public void setCarnot_modeltype(carnot_ModelType carnot_modeltype) {
        this.carnot_modeltype = carnot_modeltype;
    }
    public carnot_ContextType getCarnot_contexttype() {
        return carnot_contexttype;
    }

    public void setCarnot_contexttype(carnot_ContextType carnot_contexttype) {
        this.carnot_contexttype = carnot_contexttype;
    }
    public List<carnot_ContextType> getCarnot_contexttypes() {
        return carnot_contexttypes;
    }

    public void addCarnot_contexttype(Carnot_contexttype carnot_contexttype) {
        this.carnot_contexttypes.add(carnot_contexttype);
    }

}






import java.util.List;
import java.util.ArrayList;

public class model_IServiceTypeID  {

    private String ecfServices;
    private String ecfScopes;
    private String ecfServiceTypeID;
    private String ecfProtocols;
    private String ecfServiceName;
    private String ecfNamingAuthority;





    private model_IServiceID model_iserviceid;


    public model_IServiceTypeID(
        String ecfServices,        String ecfScopes,        String ecfServiceTypeID,        String ecfProtocols,        String ecfServiceName,        String ecfNamingAuthority    ) {
        this.ecfServices = ecfServices;
        this.ecfScopes = ecfScopes;
        this.ecfServiceTypeID = ecfServiceTypeID;
        this.ecfProtocols = ecfProtocols;
        this.ecfServiceName = ecfServiceName;
        this.ecfNamingAuthority = ecfNamingAuthority;
    }


    public String getEcfservices() {
        return ecfServices;
    }

    public void setEcfservices(String ecfServices) {
        this.ecfServices = ecfServices;
    }
    public String getEcfscopes() {
        return ecfScopes;
    }

    public void setEcfscopes(String ecfScopes) {
        this.ecfScopes = ecfScopes;
    }
    public String getEcfservicetypeid() {
        return ecfServiceTypeID;
    }

    public void setEcfservicetypeid(String ecfServiceTypeID) {
        this.ecfServiceTypeID = ecfServiceTypeID;
    }
    public String getEcfprotocols() {
        return ecfProtocols;
    }

    public void setEcfprotocols(String ecfProtocols) {
        this.ecfProtocols = ecfProtocols;
    }
    public String getEcfservicename() {
        return ecfServiceName;
    }

    public void setEcfservicename(String ecfServiceName) {
        this.ecfServiceName = ecfServiceName;
    }
    public String getEcfnamingauthority() {
        return ecfNamingAuthority;
    }

    public void setEcfnamingauthority(String ecfNamingAuthority) {
        this.ecfNamingAuthority = ecfNamingAuthority;
    }

    public model_IServiceID getModel_iserviceid() {
        return model_iserviceid;
    }

    public void setModel_iserviceid(model_IServiceID model_iserviceid) {
        this.model_iserviceid = model_iserviceid;
    }

}
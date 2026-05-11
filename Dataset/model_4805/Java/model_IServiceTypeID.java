





import java.util.List;
import java.util.ArrayList;

public class model_IServiceTypeID  {

    private String ecfServiceTypeID;
    private String ecfProtocols;
    private String ecfServiceName;
    private String ecfServices;
    private String ecfNamingAuthority;
    private String ecfScopes;



    public model_IServiceTypeID(
        String ecfServiceTypeID,        String ecfProtocols,        String ecfServiceName,        String ecfServices,        String ecfNamingAuthority,        String ecfScopes    ) {
        this.ecfServiceTypeID = ecfServiceTypeID;
        this.ecfProtocols = ecfProtocols;
        this.ecfServiceName = ecfServiceName;
        this.ecfServices = ecfServices;
        this.ecfNamingAuthority = ecfNamingAuthority;
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
    public String getEcfservices() {
        return ecfServices;
    }

    public void setEcfservices(String ecfServices) {
        this.ecfServices = ecfServices;
    }
    public String getEcfnamingauthority() {
        return ecfNamingAuthority;
    }

    public void setEcfnamingauthority(String ecfNamingAuthority) {
        this.ecfNamingAuthority = ecfNamingAuthority;
    }
    public String getEcfscopes() {
        return ecfScopes;
    }

    public void setEcfscopes(String ecfScopes) {
        this.ecfScopes = ecfScopes;
    }


}
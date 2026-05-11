





import java.util.List;
import java.util.ArrayList;

public class application_OAuthConfig extends Security {

    private String useScopeInterfaceOnRedirect;





    private List<application_OAuthClientConfig> application_oauthclientconfigs;




    private List<application_OAuthAdmin> application_oauthadmins;


    public application_OAuthConfig(
        String useScopeInterfaceOnRedirect    ) {
        super(
        );
        this.useScopeInterfaceOnRedirect = useScopeInterfaceOnRedirect;
        this.application_oauthclientconfigs = new ArrayList<>();
        this.application_oauthadmins = new ArrayList<>();
    }

    public application_OAuthConfig(
        String useScopeInterfaceOnRedirect        ArrayList<application_OAuthClientConfig> application_oauthclientconfigs,        ArrayList<application_OAuthAdmin> application_oauthadmins    ) {
        this.useScopeInterfaceOnRedirect = useScopeInterfaceOnRedirect;
        this.application_oauthclientconfigs = application_oauthclientconfigs;
        this.application_oauthadmins = application_oauthadmins;
    }

    public String getUsescopeinterfaceonredirect() {
        return useScopeInterfaceOnRedirect;
    }

    public void setUsescopeinterfaceonredirect(String useScopeInterfaceOnRedirect) {
        this.useScopeInterfaceOnRedirect = useScopeInterfaceOnRedirect;
    }

    public List<application_OAuthClientConfig> getApplication_oauthclientconfigs() {
        return application_oauthclientconfigs;
    }

    public void addApplication_oauthclientconfig(Application_oauthclientconfig application_oauthclientconfig) {
        this.application_oauthclientconfigs.add(application_oauthclientconfig);
    }
    public List<application_OAuthAdmin> getApplication_oauthadmins() {
        return application_oauthadmins;
    }

    public void addApplication_oauthadmin(Application_oauthadmin application_oauthadmin) {
        this.application_oauthadmins.add(application_oauthadmin);
    }

}
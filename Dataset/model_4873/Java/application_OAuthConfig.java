





import java.util.List;
import java.util.ArrayList;

public class application_OAuthConfig extends Security {

    private String useScopeInterfaceOnRedirect;



    public application_OAuthConfig(
        String useScopeInterfaceOnRedirect    ) {
        super(
        );
        this.useScopeInterfaceOnRedirect = useScopeInterfaceOnRedirect;
    }


    public String getUsescopeinterfaceonredirect() {
        return useScopeInterfaceOnRedirect;
    }

    public void setUsescopeinterfaceonredirect(String useScopeInterfaceOnRedirect) {
        this.useScopeInterfaceOnRedirect = useScopeInterfaceOnRedirect;
    }


}
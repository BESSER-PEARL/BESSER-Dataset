





import java.util.List;
import java.util.ArrayList;

public class application_OAuthAdmin  {

    private String username;
    private String passwordHash;





    private application_OAuthConfig application_oauthconfig;


    public application_OAuthAdmin(
        String username,        String passwordHash    ) {
        this.username = username;
        this.passwordHash = passwordHash;
    }


    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getPasswordhash() {
        return passwordHash;
    }

    public void setPasswordhash(String passwordHash) {
        this.passwordHash = passwordHash;
    }

    public application_OAuthConfig getApplication_oauthconfig() {
        return application_oauthconfig;
    }

    public void setApplication_oauthconfig(application_OAuthConfig application_oauthconfig) {
        this.application_oauthconfig = application_oauthconfig;
    }

}
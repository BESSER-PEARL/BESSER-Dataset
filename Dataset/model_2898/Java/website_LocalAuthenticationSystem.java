





import java.util.List;
import java.util.ArrayList;

public class website_LocalAuthenticationSystem extends Authentication {

    private boolean useCaptcha;
    private boolean allowSelfRegistration;
    private boolean trackLoginAttempts;
    private boolean sendWelcomeEmail;
    private String authenticationKey;
    private boolean allowRememberMe;
    private boolean useEmailActivation;





    private website_EntityOrView website_entityorview;


    public website_LocalAuthenticationSystem(
        boolean useCaptcha,        boolean allowSelfRegistration,        boolean trackLoginAttempts,        boolean sendWelcomeEmail,        String authenticationKey,        boolean allowRememberMe,        boolean useEmailActivation    ) {
        super(
        );
        this.useCaptcha = useCaptcha;
        this.allowSelfRegistration = allowSelfRegistration;
        this.trackLoginAttempts = trackLoginAttempts;
        this.sendWelcomeEmail = sendWelcomeEmail;
        this.authenticationKey = authenticationKey;
        this.allowRememberMe = allowRememberMe;
        this.useEmailActivation = useEmailActivation;
    }


    public boolean getUsecaptcha() {
        return useCaptcha;
    }

    public void setUsecaptcha(boolean useCaptcha) {
        this.useCaptcha = useCaptcha;
    }
    public boolean getAllowselfregistration() {
        return allowSelfRegistration;
    }

    public void setAllowselfregistration(boolean allowSelfRegistration) {
        this.allowSelfRegistration = allowSelfRegistration;
    }
    public boolean getTrackloginattempts() {
        return trackLoginAttempts;
    }

    public void setTrackloginattempts(boolean trackLoginAttempts) {
        this.trackLoginAttempts = trackLoginAttempts;
    }
    public boolean getSendwelcomeemail() {
        return sendWelcomeEmail;
    }

    public void setSendwelcomeemail(boolean sendWelcomeEmail) {
        this.sendWelcomeEmail = sendWelcomeEmail;
    }
    public String getAuthenticationkey() {
        return authenticationKey;
    }

    public void setAuthenticationkey(String authenticationKey) {
        this.authenticationKey = authenticationKey;
    }
    public boolean getAllowrememberme() {
        return allowRememberMe;
    }

    public void setAllowrememberme(boolean allowRememberMe) {
        this.allowRememberMe = allowRememberMe;
    }
    public boolean getUseemailactivation() {
        return useEmailActivation;
    }

    public void setUseemailactivation(boolean useEmailActivation) {
        this.useEmailActivation = useEmailActivation;
    }

    public website_EntityOrView getWebsite_entityorview() {
        return website_entityorview;
    }

    public void setWebsite_entityorview(website_EntityOrView website_entityorview) {
        this.website_entityorview = website_entityorview;
    }

}
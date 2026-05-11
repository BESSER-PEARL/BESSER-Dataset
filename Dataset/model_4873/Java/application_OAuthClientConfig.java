




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class application_OAuthClientConfig  {

    private String code;
    private LocalDate accessTokenExpirationDate;
    private LocalDate accessTokenCreationDate;
    private String type;
    private String redirectionURL;
    private String description;
    private String clientID;
    private String allowedMetaTags;
    private String refreshToken;
    private String forbiddenMetaTags;
    private String grantType;
    private String accessToken;
    private String oAuthScopeLevel;
    private String name;
    private String clientSecret;





    private application_OAuthConfig application_oauthconfig;


    public application_OAuthClientConfig(
        String code,        LocalDate accessTokenExpirationDate,        LocalDate accessTokenCreationDate,        String type,        String redirectionURL,        String description,        String clientID,        String allowedMetaTags,        String refreshToken,        String forbiddenMetaTags,        String grantType,        String accessToken,        String oAuthScopeLevel,        String name,        String clientSecret    ) {
        this.code = code;
        this.accessTokenExpirationDate = accessTokenExpirationDate;
        this.accessTokenCreationDate = accessTokenCreationDate;
        this.type = type;
        this.redirectionURL = redirectionURL;
        this.description = description;
        this.clientID = clientID;
        this.allowedMetaTags = allowedMetaTags;
        this.refreshToken = refreshToken;
        this.forbiddenMetaTags = forbiddenMetaTags;
        this.grantType = grantType;
        this.accessToken = accessToken;
        this.oAuthScopeLevel = oAuthScopeLevel;
        this.name = name;
        this.clientSecret = clientSecret;
    }


    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public LocalDate getAccesstokenexpirationdate() {
        return accessTokenExpirationDate;
    }

    public void setAccesstokenexpirationdate(LocalDate accessTokenExpirationDate) {
        this.accessTokenExpirationDate = accessTokenExpirationDate;
    }
    public LocalDate getAccesstokencreationdate() {
        return accessTokenCreationDate;
    }

    public void setAccesstokencreationdate(LocalDate accessTokenCreationDate) {
        this.accessTokenCreationDate = accessTokenCreationDate;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getRedirectionurl() {
        return redirectionURL;
    }

    public void setRedirectionurl(String redirectionURL) {
        this.redirectionURL = redirectionURL;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getClientid() {
        return clientID;
    }

    public void setClientid(String clientID) {
        this.clientID = clientID;
    }
    public String getAllowedmetatags() {
        return allowedMetaTags;
    }

    public void setAllowedmetatags(String allowedMetaTags) {
        this.allowedMetaTags = allowedMetaTags;
    }
    public String getRefreshtoken() {
        return refreshToken;
    }

    public void setRefreshtoken(String refreshToken) {
        this.refreshToken = refreshToken;
    }
    public String getForbiddenmetatags() {
        return forbiddenMetaTags;
    }

    public void setForbiddenmetatags(String forbiddenMetaTags) {
        this.forbiddenMetaTags = forbiddenMetaTags;
    }
    public String getGranttype() {
        return grantType;
    }

    public void setGranttype(String grantType) {
        this.grantType = grantType;
    }
    public String getAccesstoken() {
        return accessToken;
    }

    public void setAccesstoken(String accessToken) {
        this.accessToken = accessToken;
    }
    public String getOauthscopelevel() {
        return oAuthScopeLevel;
    }

    public void setOauthscopelevel(String oAuthScopeLevel) {
        this.oAuthScopeLevel = oAuthScopeLevel;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getClientsecret() {
        return clientSecret;
    }

    public void setClientsecret(String clientSecret) {
        this.clientSecret = clientSecret;
    }

    public application_OAuthConfig getApplication_oauthconfig() {
        return application_oauthconfig;
    }

    public void setApplication_oauthconfig(application_OAuthConfig application_oauthconfig) {
        this.application_oauthconfig = application_oauthconfig;
    }

}
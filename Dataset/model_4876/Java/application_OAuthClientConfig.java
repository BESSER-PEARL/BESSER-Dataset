




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class application_OAuthClientConfig  {

    private String refreshToken;
    private String allowedMetaTags;
    private String clientID;
    private String clientSecret;
    private String forbiddenMetaTags;
    private String code;
    private String accessToken;
    private String redirectionURL;
    private LocalDate accessTokenExpirationDate;
    private String oAuthScopeLevel;
    private String name;
    private String grantType;
    private String description;
    private String type;
    private LocalDate accessTokenCreationDate;





    private application_OAuthConfig application_oauthconfig;




    private application_OAuthClientScope application_oauthclientscope;


    public application_OAuthClientConfig(
        String refreshToken,        String allowedMetaTags,        String clientID,        String clientSecret,        String forbiddenMetaTags,        String code,        String accessToken,        String redirectionURL,        LocalDate accessTokenExpirationDate,        String oAuthScopeLevel,        String name,        String grantType,        String description,        String type,        LocalDate accessTokenCreationDate    ) {
        this.refreshToken = refreshToken;
        this.allowedMetaTags = allowedMetaTags;
        this.clientID = clientID;
        this.clientSecret = clientSecret;
        this.forbiddenMetaTags = forbiddenMetaTags;
        this.code = code;
        this.accessToken = accessToken;
        this.redirectionURL = redirectionURL;
        this.accessTokenExpirationDate = accessTokenExpirationDate;
        this.oAuthScopeLevel = oAuthScopeLevel;
        this.name = name;
        this.grantType = grantType;
        this.description = description;
        this.type = type;
        this.accessTokenCreationDate = accessTokenCreationDate;
    }


    public String getRefreshtoken() {
        return refreshToken;
    }

    public void setRefreshtoken(String refreshToken) {
        this.refreshToken = refreshToken;
    }
    public String getAllowedmetatags() {
        return allowedMetaTags;
    }

    public void setAllowedmetatags(String allowedMetaTags) {
        this.allowedMetaTags = allowedMetaTags;
    }
    public String getClientid() {
        return clientID;
    }

    public void setClientid(String clientID) {
        this.clientID = clientID;
    }
    public String getClientsecret() {
        return clientSecret;
    }

    public void setClientsecret(String clientSecret) {
        this.clientSecret = clientSecret;
    }
    public String getForbiddenmetatags() {
        return forbiddenMetaTags;
    }

    public void setForbiddenmetatags(String forbiddenMetaTags) {
        this.forbiddenMetaTags = forbiddenMetaTags;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getAccesstoken() {
        return accessToken;
    }

    public void setAccesstoken(String accessToken) {
        this.accessToken = accessToken;
    }
    public String getRedirectionurl() {
        return redirectionURL;
    }

    public void setRedirectionurl(String redirectionURL) {
        this.redirectionURL = redirectionURL;
    }
    public LocalDate getAccesstokenexpirationdate() {
        return accessTokenExpirationDate;
    }

    public void setAccesstokenexpirationdate(LocalDate accessTokenExpirationDate) {
        this.accessTokenExpirationDate = accessTokenExpirationDate;
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
    public String getGranttype() {
        return grantType;
    }

    public void setGranttype(String grantType) {
        this.grantType = grantType;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public LocalDate getAccesstokencreationdate() {
        return accessTokenCreationDate;
    }

    public void setAccesstokencreationdate(LocalDate accessTokenCreationDate) {
        this.accessTokenCreationDate = accessTokenCreationDate;
    }

    public application_OAuthConfig getApplication_oauthconfig() {
        return application_oauthconfig;
    }

    public void setApplication_oauthconfig(application_OAuthConfig application_oauthconfig) {
        this.application_oauthconfig = application_oauthconfig;
    }
    public application_OAuthClientScope getApplication_oauthclientscope() {
        return application_oauthclientscope;
    }

    public void setApplication_oauthclientscope(application_OAuthClientScope application_oauthclientscope) {
        this.application_oauthclientscope = application_oauthclientscope;
    }

}





import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class application_OAuthClientConfig  {

    private String description;
    private String allowedMetaTags;
    private String clientSecret;
    private LocalDate accessTokenExpirationDate;
    private String oAuthScopeLevel;
    private String name;
    private String redirectionURL;
    private String type;
    private String clientID;
    private String forbiddenMetaTags;
    private String accessToken;
    private String code;
    private LocalDate accessTokenCreationDate;
    private String refreshToken;
    private String grantType;





    private application_OAuthClientScope application_oauthclientscope;




    private application_OAuthConfig application_oauthconfig;


    public application_OAuthClientConfig(
        String description,        String allowedMetaTags,        String clientSecret,        LocalDate accessTokenExpirationDate,        String oAuthScopeLevel,        String name,        String redirectionURL,        String type,        String clientID,        String forbiddenMetaTags,        String accessToken,        String code,        LocalDate accessTokenCreationDate,        String refreshToken,        String grantType    ) {
        this.description = description;
        this.allowedMetaTags = allowedMetaTags;
        this.clientSecret = clientSecret;
        this.accessTokenExpirationDate = accessTokenExpirationDate;
        this.oAuthScopeLevel = oAuthScopeLevel;
        this.name = name;
        this.redirectionURL = redirectionURL;
        this.type = type;
        this.clientID = clientID;
        this.forbiddenMetaTags = forbiddenMetaTags;
        this.accessToken = accessToken;
        this.code = code;
        this.accessTokenCreationDate = accessTokenCreationDate;
        this.refreshToken = refreshToken;
        this.grantType = grantType;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getAllowedmetatags() {
        return allowedMetaTags;
    }

    public void setAllowedmetatags(String allowedMetaTags) {
        this.allowedMetaTags = allowedMetaTags;
    }
    public String getClientsecret() {
        return clientSecret;
    }

    public void setClientsecret(String clientSecret) {
        this.clientSecret = clientSecret;
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
    public String getRedirectionurl() {
        return redirectionURL;
    }

    public void setRedirectionurl(String redirectionURL) {
        this.redirectionURL = redirectionURL;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getClientid() {
        return clientID;
    }

    public void setClientid(String clientID) {
        this.clientID = clientID;
    }
    public String getForbiddenmetatags() {
        return forbiddenMetaTags;
    }

    public void setForbiddenmetatags(String forbiddenMetaTags) {
        this.forbiddenMetaTags = forbiddenMetaTags;
    }
    public String getAccesstoken() {
        return accessToken;
    }

    public void setAccesstoken(String accessToken) {
        this.accessToken = accessToken;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public LocalDate getAccesstokencreationdate() {
        return accessTokenCreationDate;
    }

    public void setAccesstokencreationdate(LocalDate accessTokenCreationDate) {
        this.accessTokenCreationDate = accessTokenCreationDate;
    }
    public String getRefreshtoken() {
        return refreshToken;
    }

    public void setRefreshtoken(String refreshToken) {
        this.refreshToken = refreshToken;
    }
    public String getGranttype() {
        return grantType;
    }

    public void setGranttype(String grantType) {
        this.grantType = grantType;
    }

    public application_OAuthClientScope getApplication_oauthclientscope() {
        return application_oauthclientscope;
    }

    public void setApplication_oauthclientscope(application_OAuthClientScope application_oauthclientscope) {
        this.application_oauthclientscope = application_oauthclientscope;
    }
    public application_OAuthConfig getApplication_oauthconfig() {
        return application_oauthconfig;
    }

    public void setApplication_oauthconfig(application_OAuthConfig application_oauthconfig) {
        this.application_oauthconfig = application_oauthconfig;
    }

}
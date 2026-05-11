




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class application_OAuthClientConfig  {

    private String type;
    private String refreshToken;
    private String name;
    private LocalDate accessTokenCreationDate;
    private String accessToken;
    private String forbiddenMetaTags;
    private String description;
    private String code;
    private String clientSecret;
    private LocalDate accessTokenExpirationDate;
    private String oAuthScopeLevel;
    private String redirectionURL;
    private String grantType;
    private String allowedMetaTags;
    private String clientID;



    public application_OAuthClientConfig(
        String type,        String refreshToken,        String name,        LocalDate accessTokenCreationDate,        String accessToken,        String forbiddenMetaTags,        String description,        String code,        String clientSecret,        LocalDate accessTokenExpirationDate,        String oAuthScopeLevel,        String redirectionURL,        String grantType,        String allowedMetaTags,        String clientID    ) {
        this.type = type;
        this.refreshToken = refreshToken;
        this.name = name;
        this.accessTokenCreationDate = accessTokenCreationDate;
        this.accessToken = accessToken;
        this.forbiddenMetaTags = forbiddenMetaTags;
        this.description = description;
        this.code = code;
        this.clientSecret = clientSecret;
        this.accessTokenExpirationDate = accessTokenExpirationDate;
        this.oAuthScopeLevel = oAuthScopeLevel;
        this.redirectionURL = redirectionURL;
        this.grantType = grantType;
        this.allowedMetaTags = allowedMetaTags;
        this.clientID = clientID;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getRefreshtoken() {
        return refreshToken;
    }

    public void setRefreshtoken(String refreshToken) {
        this.refreshToken = refreshToken;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public LocalDate getAccesstokencreationdate() {
        return accessTokenCreationDate;
    }

    public void setAccesstokencreationdate(LocalDate accessTokenCreationDate) {
        this.accessTokenCreationDate = accessTokenCreationDate;
    }
    public String getAccesstoken() {
        return accessToken;
    }

    public void setAccesstoken(String accessToken) {
        this.accessToken = accessToken;
    }
    public String getForbiddenmetatags() {
        return forbiddenMetaTags;
    }

    public void setForbiddenmetatags(String forbiddenMetaTags) {
        this.forbiddenMetaTags = forbiddenMetaTags;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
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
    public String getRedirectionurl() {
        return redirectionURL;
    }

    public void setRedirectionurl(String redirectionURL) {
        this.redirectionURL = redirectionURL;
    }
    public String getGranttype() {
        return grantType;
    }

    public void setGranttype(String grantType) {
        this.grantType = grantType;
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


}
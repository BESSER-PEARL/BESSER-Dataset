





import java.util.List;
import java.util.ArrayList;

public class commons_Organization extends SchemaVersionable, Identifiable, NameContainer {

    private String twitterId;
    private String twitterScreenName;
    private String facebookAccessToken;
    private String facebookUserName;
    private String twitterAccessTokenSecret;
    private String facebookPageUri;
    private String twitterAccessToken;
    private String schemaVersion;
    private String blackBerryPin;
    private String website;
    private String facebookId;



    public commons_Organization(
        String twitterId,        String twitterScreenName,        String facebookAccessToken,        String facebookUserName,        String twitterAccessTokenSecret,        String facebookPageUri,        String twitterAccessToken,        String schemaVersion,        String blackBerryPin,        String website,        String facebookId    ) {
        super(
        );
        this.twitterId = twitterId;
        this.twitterScreenName = twitterScreenName;
        this.facebookAccessToken = facebookAccessToken;
        this.facebookUserName = facebookUserName;
        this.twitterAccessTokenSecret = twitterAccessTokenSecret;
        this.facebookPageUri = facebookPageUri;
        this.twitterAccessToken = twitterAccessToken;
        this.schemaVersion = schemaVersion;
        this.blackBerryPin = blackBerryPin;
        this.website = website;
        this.facebookId = facebookId;
    }


    public String getTwitterid() {
        return twitterId;
    }

    public void setTwitterid(String twitterId) {
        this.twitterId = twitterId;
    }
    public String getTwitterscreenname() {
        return twitterScreenName;
    }

    public void setTwitterscreenname(String twitterScreenName) {
        this.twitterScreenName = twitterScreenName;
    }
    public String getFacebookaccesstoken() {
        return facebookAccessToken;
    }

    public void setFacebookaccesstoken(String facebookAccessToken) {
        this.facebookAccessToken = facebookAccessToken;
    }
    public String getFacebookusername() {
        return facebookUserName;
    }

    public void setFacebookusername(String facebookUserName) {
        this.facebookUserName = facebookUserName;
    }
    public String getTwitteraccesstokensecret() {
        return twitterAccessTokenSecret;
    }

    public void setTwitteraccesstokensecret(String twitterAccessTokenSecret) {
        this.twitterAccessTokenSecret = twitterAccessTokenSecret;
    }
    public String getFacebookpageuri() {
        return facebookPageUri;
    }

    public void setFacebookpageuri(String facebookPageUri) {
        this.facebookPageUri = facebookPageUri;
    }
    public String getTwitteraccesstoken() {
        return twitterAccessToken;
    }

    public void setTwitteraccesstoken(String twitterAccessToken) {
        this.twitterAccessToken = twitterAccessToken;
    }
    public String getSchemaversion() {
        return schemaVersion;
    }

    public void setSchemaversion(String schemaVersion) {
        this.schemaVersion = schemaVersion;
    }
    public String getBlackberrypin() {
        return blackBerryPin;
    }

    public void setBlackberrypin(String blackBerryPin) {
        this.blackBerryPin = blackBerryPin;
    }
    public String getWebsite() {
        return website;
    }

    public void setWebsite(String website) {
        this.website = website;
    }
    public String getFacebookid() {
        return facebookId;
    }

    public void setFacebookid(String facebookId) {
        this.facebookId = facebookId;
    }


}
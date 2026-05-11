





import java.util.List;
import java.util.ArrayList;

public class commons_TwitterAccessible  {

    private String twitterAccessToken;
    private String twitterAccessTokenSecret;



    public commons_TwitterAccessible(
        String twitterAccessToken,        String twitterAccessTokenSecret    ) {
        this.twitterAccessToken = twitterAccessToken;
        this.twitterAccessTokenSecret = twitterAccessTokenSecret;
    }


    public String getTwitteraccesstoken() {
        return twitterAccessToken;
    }

    public void setTwitteraccesstoken(String twitterAccessToken) {
        this.twitterAccessToken = twitterAccessToken;
    }
    public String getTwitteraccesstokensecret() {
        return twitterAccessTokenSecret;
    }

    public void setTwitteraccesstokensecret(String twitterAccessTokenSecret) {
        this.twitterAccessTokenSecret = twitterAccessTokenSecret;
    }


}
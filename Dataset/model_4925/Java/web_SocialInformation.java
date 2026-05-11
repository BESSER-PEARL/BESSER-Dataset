





import java.util.List;
import java.util.ArrayList;

public class web_SocialInformation  {

    private String facebookUrl;
    private String plusUrl;
    private String twitterUrl;
    private String url;





    private web_SocialBar web_socialbar;


    public web_SocialInformation(
        String facebookUrl,        String plusUrl,        String twitterUrl,        String url    ) {
        this.facebookUrl = facebookUrl;
        this.plusUrl = plusUrl;
        this.twitterUrl = twitterUrl;
        this.url = url;
    }


    public String getFacebookurl() {
        return facebookUrl;
    }

    public void setFacebookurl(String facebookUrl) {
        this.facebookUrl = facebookUrl;
    }
    public String getPlusurl() {
        return plusUrl;
    }

    public void setPlusurl(String plusUrl) {
        this.plusUrl = plusUrl;
    }
    public String getTwitterurl() {
        return twitterUrl;
    }

    public void setTwitterurl(String twitterUrl) {
        this.twitterUrl = twitterUrl;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public web_SocialBar getWeb_socialbar() {
        return web_socialbar;
    }

    public void setWeb_socialbar(web_SocialBar web_socialbar) {
        this.web_socialbar = web_socialbar;
    }

}
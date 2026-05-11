





import java.util.List;
import java.util.ArrayList;

public class commons_TwitterIdentity  {

    private String twitterId;
    private String twitterScreenName;



    public commons_TwitterIdentity(
        String twitterId,        String twitterScreenName    ) {
        this.twitterId = twitterId;
        this.twitterScreenName = twitterScreenName;
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


}
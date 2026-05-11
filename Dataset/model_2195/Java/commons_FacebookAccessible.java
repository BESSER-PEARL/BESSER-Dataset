





import java.util.List;
import java.util.ArrayList;

public class commons_FacebookAccessible  {

    private String facebookAccessToken;



    public commons_FacebookAccessible(
        String facebookAccessToken    ) {
        this.facebookAccessToken = facebookAccessToken;
    }


    public String getFacebookaccesstoken() {
        return facebookAccessToken;
    }

    public void setFacebookaccesstoken(String facebookAccessToken) {
        this.facebookAccessToken = facebookAccessToken;
    }


}
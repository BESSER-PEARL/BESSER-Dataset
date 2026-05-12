





import java.util.List;
import java.util.ArrayList;

public class JLGCurrentUserRestResource  {

    private String formURL;
    private String visitorId;



    public JLGCurrentUserRestResource(
        String formURL,        String visitorId    ) {
        this.formURL = formURL;
        this.visitorId = visitorId;
    }


    public String getFormurl() {
        return formURL;
    }

    public void setFormurl(String formURL) {
        this.formURL = formURL;
    }
    public String getVisitorid() {
        return visitorId;
    }

    public void setVisitorid(String visitorId) {
        this.visitorId = visitorId;
    }


}
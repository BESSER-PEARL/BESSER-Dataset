





import java.util.List;
import java.util.ArrayList;

public class webapp_WebConfig  {

    private String displayName;





    private webapp_WebApp webapp_webapp;


    public webapp_WebConfig(
        String displayName    ) {
        this.displayName = displayName;
    }


    public String getDisplayname() {
        return displayName;
    }

    public void setDisplayname(String displayName) {
        this.displayName = displayName;
    }

    public webapp_WebApp getWebapp_webapp() {
        return webapp_webapp;
    }

    public void setWebapp_webapp(webapp_WebApp webapp_webapp) {
        this.webapp_webapp = webapp_webapp;
    }

}
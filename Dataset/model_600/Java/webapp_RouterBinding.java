





import java.util.List;
import java.util.ArrayList;

public class webapp_RouterBinding  {

    private String requestURL;
    private String requestCookies;





    private webapp_Controller webapp_controller;




    private webapp_Router webapp_router;


    public webapp_RouterBinding(
        String requestURL,        String requestCookies    ) {
        this.requestURL = requestURL;
        this.requestCookies = requestCookies;
    }


    public String getRequesturl() {
        return requestURL;
    }

    public void setRequesturl(String requestURL) {
        this.requestURL = requestURL;
    }
    public String getRequestcookies() {
        return requestCookies;
    }

    public void setRequestcookies(String requestCookies) {
        this.requestCookies = requestCookies;
    }

    public webapp_Controller getWebapp_controller() {
        return webapp_controller;
    }

    public void setWebapp_controller(webapp_Controller webapp_controller) {
        this.webapp_controller = webapp_controller;
    }
    public webapp_Router getWebapp_router() {
        return webapp_router;
    }

    public void setWebapp_router(webapp_Router webapp_router) {
        this.webapp_router = webapp_router;
    }

}
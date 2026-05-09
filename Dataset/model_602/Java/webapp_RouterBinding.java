





import java.util.List;
import java.util.ArrayList;

public class webapp_RouterBinding  {

    private String url;





    private webapp_Router webapp_router;




    private webapp_Controller webapp_controller;


    public webapp_RouterBinding(
        String url    ) {
        this.url = url;
    }


    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public webapp_Router getWebapp_router() {
        return webapp_router;
    }

    public void setWebapp_router(webapp_Router webapp_router) {
        this.webapp_router = webapp_router;
    }
    public webapp_Controller getWebapp_controller() {
        return webapp_controller;
    }

    public void setWebapp_controller(webapp_Controller webapp_controller) {
        this.webapp_controller = webapp_controller;
    }

}
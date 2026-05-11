





import java.util.List;
import java.util.ArrayList;

public class webapp_RouterMapping  {

    private String path;





    private webapp_AbstractView webapp_abstractview;




    private webapp_Router webapp_router;


    public webapp_RouterMapping(
        String path    ) {
        this.path = path;
    }


    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }

    public webapp_AbstractView getWebapp_abstractview() {
        return webapp_abstractview;
    }

    public void setWebapp_abstractview(webapp_AbstractView webapp_abstractview) {
        this.webapp_abstractview = webapp_abstractview;
    }
    public webapp_Router getWebapp_router() {
        return webapp_router;
    }

    public void setWebapp_router(webapp_Router webapp_router) {
        this.webapp_router = webapp_router;
    }

}
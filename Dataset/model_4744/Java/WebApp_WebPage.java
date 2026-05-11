





import java.util.List;
import java.util.ArrayList;

public class WebApp_WebPage  {

    private String name;





    private WebApp_WebPage webapp_webpage;




    private WebApp_WebApp webapp_webapp;


    public WebApp_WebPage(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public WebApp_WebPage getWebapp_webpage() {
        return webapp_webpage;
    }

    public void setWebapp_webpage(WebApp_WebPage webapp_webpage) {
        this.webapp_webpage = webapp_webpage;
    }
    public WebApp_WebApp getWebapp_webapp() {
        return webapp_webapp;
    }

    public void setWebapp_webapp(WebApp_WebApp webapp_webapp) {
        this.webapp_webapp = webapp_webapp;
    }

}
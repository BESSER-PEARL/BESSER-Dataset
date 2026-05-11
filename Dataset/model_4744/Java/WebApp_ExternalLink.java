





import java.util.List;
import java.util.ArrayList;

public class WebApp_ExternalLink  {

    private String url;





    private WebApp_WebPage webapp_webpage;


    public WebApp_ExternalLink(
        String url    ) {
        this.url = url;
    }


    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public WebApp_WebPage getWebapp_webpage() {
        return webapp_webpage;
    }

    public void setWebapp_webpage(WebApp_WebPage webapp_webpage) {
        this.webapp_webpage = webapp_webpage;
    }

}
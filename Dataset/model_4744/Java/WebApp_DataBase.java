





import java.util.List;
import java.util.ArrayList;

public class WebApp_DataBase  {






    private List<WebApp_Entity> webapp_entitys;




    private WebApp_WebApp webapp_webapp;


    public WebApp_DataBase(
    ) {
        this.webapp_entitys = new ArrayList<>();
    }

    public WebApp_DataBase(
        ArrayList<WebApp_Entity> webapp_entitys    ) {
        this.webapp_entitys = webapp_entitys;
    }


    public List<WebApp_Entity> getWebapp_entitys() {
        return webapp_entitys;
    }

    public void addWebapp_entity(Webapp_entity webapp_entity) {
        this.webapp_entitys.add(webapp_entity);
    }
    public WebApp_WebApp getWebapp_webapp() {
        return webapp_webapp;
    }

    public void setWebapp_webapp(WebApp_WebApp webapp_webapp) {
        this.webapp_webapp = webapp_webapp;
    }

}
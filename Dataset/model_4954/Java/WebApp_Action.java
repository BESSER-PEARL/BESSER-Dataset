





import java.util.List;
import java.util.ArrayList;

public class WebApp_Action extends NamedElement {






    private List<WebApp_Entities> webapp_entitiess;




    private WebApp_Pages webapp_pages;




    private WebApp_Controller webapp_controller;


    public WebApp_Action(
    ) {
        super(
        );
        this.webapp_entitiess = new ArrayList<>();
    }

    public WebApp_Action(
        ArrayList<WebApp_Entities> webapp_entitiess    ) {
        this.webapp_entitiess = webapp_entitiess;
    }


    public List<WebApp_Entities> getWebapp_entitiess() {
        return webapp_entitiess;
    }

    public void addWebapp_entities(Webapp_entities webapp_entities) {
        this.webapp_entitiess.add(webapp_entities);
    }
    public WebApp_Pages getWebapp_pages() {
        return webapp_pages;
    }

    public void setWebapp_pages(WebApp_Pages webapp_pages) {
        this.webapp_pages = webapp_pages;
    }
    public WebApp_Controller getWebapp_controller() {
        return webapp_controller;
    }

    public void setWebapp_controller(WebApp_Controller webapp_controller) {
        this.webapp_controller = webapp_controller;
    }

}
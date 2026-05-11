





import java.util.List;
import java.util.ArrayList;

public class WebApp_Views extends IdElement, NamedElement {






    private WebApp_Entities webapp_entities;




    private List<WebApp_Forms> webapp_formss;




    private List<WebApp_styleElements> webapp_styleelementss;




    private List<WebApp_Tables> webapp_tabless;




    private WebApp_Pages webapp_pages;


    public WebApp_Views(
    ) {
        super(
        );
        this.webapp_formss = new ArrayList<>();
        this.webapp_styleelementss = new ArrayList<>();
        this.webapp_tabless = new ArrayList<>();
    }

    public WebApp_Views(
        ArrayList<WebApp_Forms> webapp_formss,        ArrayList<WebApp_styleElements> webapp_styleelementss,        ArrayList<WebApp_Tables> webapp_tabless    ) {
        this.webapp_formss = webapp_formss;
        this.webapp_styleelementss = webapp_styleelementss;
        this.webapp_tabless = webapp_tabless;
    }


    public WebApp_Entities getWebapp_entities() {
        return webapp_entities;
    }

    public void setWebapp_entities(WebApp_Entities webapp_entities) {
        this.webapp_entities = webapp_entities;
    }
    public List<WebApp_Forms> getWebapp_formss() {
        return webapp_formss;
    }

    public void addWebapp_forms(Webapp_forms webapp_forms) {
        this.webapp_formss.add(webapp_forms);
    }
    public List<WebApp_styleElements> getWebapp_styleelementss() {
        return webapp_styleelementss;
    }

    public void addWebapp_styleelements(Webapp_styleelements webapp_styleelements) {
        this.webapp_styleelementss.add(webapp_styleelements);
    }
    public List<WebApp_Tables> getWebapp_tabless() {
        return webapp_tabless;
    }

    public void addWebapp_tables(Webapp_tables webapp_tables) {
        this.webapp_tabless.add(webapp_tables);
    }
    public WebApp_Pages getWebapp_pages() {
        return webapp_pages;
    }

    public void setWebapp_pages(WebApp_Pages webapp_pages) {
        this.webapp_pages = webapp_pages;
    }

}
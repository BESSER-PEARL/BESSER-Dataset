





import java.util.List;
import java.util.ArrayList;

public class webapp_ClientPage extends Named {






    private List<webapp_UIElement> webapp_uielements;




    private webapp_ServerPage webapp_serverpage;




    private webapp_WebApp webapp_webapp;




    private webapp_ServerPage webapp_serverpage;


    public webapp_ClientPage(
    ) {
        super(
        );
        this.webapp_uielements = new ArrayList<>();
    }

    public webapp_ClientPage(
        ArrayList<webapp_UIElement> webapp_uielements    ) {
        this.webapp_uielements = webapp_uielements;
    }


    public List<webapp_UIElement> getWebapp_uielements() {
        return webapp_uielements;
    }

    public void addWebapp_uielement(Webapp_uielement webapp_uielement) {
        this.webapp_uielements.add(webapp_uielement);
    }
    public webapp_ServerPage getWebapp_serverpage() {
        return webapp_serverpage;
    }

    public void setWebapp_serverpage(webapp_ServerPage webapp_serverpage) {
        this.webapp_serverpage = webapp_serverpage;
    }
    public webapp_WebApp getWebapp_webapp() {
        return webapp_webapp;
    }

    public void setWebapp_webapp(webapp_WebApp webapp_webapp) {
        this.webapp_webapp = webapp_webapp;
    }
    public webapp_ServerPage getWebapp_serverpage() {
        return webapp_serverpage;
    }

    public void setWebapp_serverpage(webapp_ServerPage webapp_serverpage) {
        this.webapp_serverpage = webapp_serverpage;
    }

}






import java.util.List;
import java.util.ArrayList;

public class webapp_View extends NamedElement {






    private List<webapp_View> webapp_views;




    private webapp_Data webapp_data;




    private webapp_WebApp webapp_webapp;


    public webapp_View(
    ) {
        super(
        );
        this.webapp_views = new ArrayList<>();
    }

    public webapp_View(
        ArrayList<webapp_View> webapp_views    ) {
        this.webapp_views = webapp_views;
    }


    public List<webapp_View> getWebapp_views() {
        return webapp_views;
    }

    public void addWebapp_view(Webapp_view webapp_view) {
        this.webapp_views.add(webapp_view);
    }
    public webapp_Data getWebapp_data() {
        return webapp_data;
    }

    public void setWebapp_data(webapp_Data webapp_data) {
        this.webapp_data = webapp_data;
    }
    public webapp_WebApp getWebapp_webapp() {
        return webapp_webapp;
    }

    public void setWebapp_webapp(webapp_WebApp webapp_webapp) {
        this.webapp_webapp = webapp_webapp;
    }

}
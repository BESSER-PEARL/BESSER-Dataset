





import java.util.List;
import java.util.ArrayList;

public class PHPMVC_coreMVC_Application  {

    private String locale;
    private String name;
    private String routes;
    private String type;



    public PHPMVC_coreMVC_Application(
        String locale,        String name,        String routes,        String type    ) {
        this.locale = locale;
        this.name = name;
        this.routes = routes;
        this.type = type;
    }


    public String getLocale() {
        return locale;
    }

    public void setLocale(String locale) {
        this.locale = locale;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getRoutes() {
        return routes;
    }

    public void setRoutes(String routes) {
        this.routes = routes;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}
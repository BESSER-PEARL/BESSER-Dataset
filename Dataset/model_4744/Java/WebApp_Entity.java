





import java.util.List;
import java.util.ArrayList;

public class WebApp_Entity  {

    private String name;





    private List<WebApp_Entity> webapp_entitys;




    private List<WebApp_Attribute> webapp_attributes;


    public WebApp_Entity(
        String name    ) {
        this.name = name;
        this.webapp_entitys = new ArrayList<>();
        this.webapp_attributes = new ArrayList<>();
    }

    public WebApp_Entity(
        String name        ArrayList<WebApp_Entity> webapp_entitys,        ArrayList<WebApp_Attribute> webapp_attributes    ) {
        this.name = name;
        this.webapp_entitys = webapp_entitys;
        this.webapp_attributes = webapp_attributes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<WebApp_Entity> getWebapp_entitys() {
        return webapp_entitys;
    }

    public void addWebapp_entity(Webapp_entity webapp_entity) {
        this.webapp_entitys.add(webapp_entity);
    }
    public List<WebApp_Attribute> getWebapp_attributes() {
        return webapp_attributes;
    }

    public void addWebapp_attribute(Webapp_attribute webapp_attribute) {
        this.webapp_attributes.add(webapp_attribute);
    }

}
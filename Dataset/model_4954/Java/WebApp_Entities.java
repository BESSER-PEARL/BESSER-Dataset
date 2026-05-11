





import java.util.List;
import java.util.ArrayList;

public class WebApp_Entities extends NamedElement {






    private List<WebApp_Dummies> webapp_dummiess;




    private WebApp_Entities webapp_entities;




    private List<WebApp_Attribute> webapp_attributes;




    private WebApp_DynamicApplication webapp_dynamicapplication;


    public WebApp_Entities(
    ) {
        super(
        );
        this.webapp_dummiess = new ArrayList<>();
        this.webapp_attributes = new ArrayList<>();
    }

    public WebApp_Entities(
        ArrayList<WebApp_Dummies> webapp_dummiess,        ArrayList<WebApp_Attribute> webapp_attributes    ) {
        this.webapp_dummiess = webapp_dummiess;
        this.webapp_attributes = webapp_attributes;
    }


    public List<WebApp_Dummies> getWebapp_dummiess() {
        return webapp_dummiess;
    }

    public void addWebapp_dummies(Webapp_dummies webapp_dummies) {
        this.webapp_dummiess.add(webapp_dummies);
    }
    public WebApp_Entities getWebapp_entities() {
        return webapp_entities;
    }

    public void setWebapp_entities(WebApp_Entities webapp_entities) {
        this.webapp_entities = webapp_entities;
    }
    public List<WebApp_Attribute> getWebapp_attributes() {
        return webapp_attributes;
    }

    public void addWebapp_attribute(Webapp_attribute webapp_attribute) {
        this.webapp_attributes.add(webapp_attribute);
    }
    public WebApp_DynamicApplication getWebapp_dynamicapplication() {
        return webapp_dynamicapplication;
    }

    public void setWebapp_dynamicapplication(WebApp_DynamicApplication webapp_dynamicapplication) {
        this.webapp_dynamicapplication = webapp_dynamicapplication;
    }

}
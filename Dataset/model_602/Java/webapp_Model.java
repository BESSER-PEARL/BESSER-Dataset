





import java.util.List;
import java.util.ArrayList;

public class webapp_Model extends Data {






    private List<webapp_Attribute> webapp_attributes;




    private webapp_WebApp webapp_webapp;




    private webapp_Collection webapp_collection;


    public webapp_Model(
    ) {
        super(
        );
        this.webapp_attributes = new ArrayList<>();
    }

    public webapp_Model(
        ArrayList<webapp_Attribute> webapp_attributes    ) {
        this.webapp_attributes = webapp_attributes;
    }


    public List<webapp_Attribute> getWebapp_attributes() {
        return webapp_attributes;
    }

    public void addWebapp_attribute(Webapp_attribute webapp_attribute) {
        this.webapp_attributes.add(webapp_attribute);
    }
    public webapp_WebApp getWebapp_webapp() {
        return webapp_webapp;
    }

    public void setWebapp_webapp(webapp_WebApp webapp_webapp) {
        this.webapp_webapp = webapp_webapp;
    }
    public webapp_Collection getWebapp_collection() {
        return webapp_collection;
    }

    public void setWebapp_collection(webapp_Collection webapp_collection) {
        this.webapp_collection = webapp_collection;
    }

}
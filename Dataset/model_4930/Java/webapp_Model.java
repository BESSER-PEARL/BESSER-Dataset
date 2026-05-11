





import java.util.List;
import java.util.ArrayList;

public class webapp_Model extends NamedElement {






    private webapp_Collection webapp_collection;




    private List<webapp_Operation> webapp_operations;




    private List<webapp_Attribute> webapp_attributes;




    private webapp_Application webapp_application;




    private webapp_Application webapp_application;


    public webapp_Model(
    ) {
        super(
        );
        this.webapp_operations = new ArrayList<>();
        this.webapp_attributes = new ArrayList<>();
    }

    public webapp_Model(
        ArrayList<webapp_Operation> webapp_operations,        ArrayList<webapp_Attribute> webapp_attributes    ) {
        this.webapp_operations = webapp_operations;
        this.webapp_attributes = webapp_attributes;
    }


    public webapp_Collection getWebapp_collection() {
        return webapp_collection;
    }

    public void setWebapp_collection(webapp_Collection webapp_collection) {
        this.webapp_collection = webapp_collection;
    }
    public List<webapp_Operation> getWebapp_operations() {
        return webapp_operations;
    }

    public void addWebapp_operation(Webapp_operation webapp_operation) {
        this.webapp_operations.add(webapp_operation);
    }
    public List<webapp_Attribute> getWebapp_attributes() {
        return webapp_attributes;
    }

    public void addWebapp_attribute(Webapp_attribute webapp_attribute) {
        this.webapp_attributes.add(webapp_attribute);
    }
    public webapp_Application getWebapp_application() {
        return webapp_application;
    }

    public void setWebapp_application(webapp_Application webapp_application) {
        this.webapp_application = webapp_application;
    }
    public webapp_Application getWebapp_application() {
        return webapp_application;
    }

    public void setWebapp_application(webapp_Application webapp_application) {
        this.webapp_application = webapp_application;
    }

}
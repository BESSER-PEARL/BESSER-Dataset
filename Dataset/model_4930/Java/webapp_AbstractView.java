





import java.util.List;
import java.util.ArrayList;

public class webapp_AbstractView extends NamedElement {

    private String description;





    private webapp_Application webapp_application;




    private List<webapp_Operation> webapp_operations;




    private webapp_Application webapp_application;


    public webapp_AbstractView(
        String description    ) {
        super(
        );
        this.description = description;
        this.webapp_operations = new ArrayList<>();
    }

    public webapp_AbstractView(
        String description        ArrayList<webapp_Operation> webapp_operations    ) {
        this.description = description;
        this.webapp_operations = webapp_operations;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public webapp_Application getWebapp_application() {
        return webapp_application;
    }

    public void setWebapp_application(webapp_Application webapp_application) {
        this.webapp_application = webapp_application;
    }
    public List<webapp_Operation> getWebapp_operations() {
        return webapp_operations;
    }

    public void addWebapp_operation(Webapp_operation webapp_operation) {
        this.webapp_operations.add(webapp_operation);
    }
    public webapp_Application getWebapp_application() {
        return webapp_application;
    }

    public void setWebapp_application(webapp_Application webapp_application) {
        this.webapp_application = webapp_application;
    }

}
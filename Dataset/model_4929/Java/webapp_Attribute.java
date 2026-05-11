





import java.util.List;
import java.util.ArrayList;

public class webapp_Attribute extends NamedElement {

    private String defaultValue;





    private webapp_Model webapp_model;


    public webapp_Attribute(
        String defaultValue    ) {
        super(
        );
        this.defaultValue = defaultValue;
    }


    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }

    public webapp_Model getWebapp_model() {
        return webapp_model;
    }

    public void setWebapp_model(webapp_Model webapp_model) {
        this.webapp_model = webapp_model;
    }

}
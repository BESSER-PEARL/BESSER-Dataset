





import java.util.List;
import java.util.ArrayList;

public class webapp_Attribute extends NamedElement {

    private String baseType;
    private String customType;





    private webapp_Controller webapp_controller;




    private webapp_View webapp_view;




    private webapp_Model webapp_model;


    public webapp_Attribute(
        String baseType,        String customType    ) {
        super(
        );
        this.baseType = baseType;
        this.customType = customType;
    }


    public String getBasetype() {
        return baseType;
    }

    public void setBasetype(String baseType) {
        this.baseType = baseType;
    }
    public String getCustomtype() {
        return customType;
    }

    public void setCustomtype(String customType) {
        this.customType = customType;
    }

    public webapp_Controller getWebapp_controller() {
        return webapp_controller;
    }

    public void setWebapp_controller(webapp_Controller webapp_controller) {
        this.webapp_controller = webapp_controller;
    }
    public webapp_View getWebapp_view() {
        return webapp_view;
    }

    public void setWebapp_view(webapp_View webapp_view) {
        this.webapp_view = webapp_view;
    }
    public webapp_Model getWebapp_model() {
        return webapp_model;
    }

    public void setWebapp_model(webapp_Model webapp_model) {
        this.webapp_model = webapp_model;
    }

}
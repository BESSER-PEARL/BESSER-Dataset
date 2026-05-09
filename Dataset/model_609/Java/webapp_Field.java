





import java.util.List;
import java.util.ArrayList;

public class webapp_Field  {

    private String defaultValue;
    private String type;
    private String name;





    private webapp_Input webapp_input;




    private webapp_BusinessObject webapp_businessobject;




    private webapp_BusinessObject webapp_businessobject;


    public webapp_Field(
        String defaultValue,        String type,        String name    ) {
        this.defaultValue = defaultValue;
        this.type = type;
        this.name = name;
    }


    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public webapp_Input getWebapp_input() {
        return webapp_input;
    }

    public void setWebapp_input(webapp_Input webapp_input) {
        this.webapp_input = webapp_input;
    }
    public webapp_BusinessObject getWebapp_businessobject() {
        return webapp_businessobject;
    }

    public void setWebapp_businessobject(webapp_BusinessObject webapp_businessobject) {
        this.webapp_businessobject = webapp_businessobject;
    }
    public webapp_BusinessObject getWebapp_businessobject() {
        return webapp_businessobject;
    }

    public void setWebapp_businessobject(webapp_BusinessObject webapp_businessobject) {
        this.webapp_businessobject = webapp_businessobject;
    }

}
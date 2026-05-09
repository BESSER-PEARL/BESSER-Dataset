





import java.util.List;
import java.util.ArrayList;

public class webapp_Input extends Tag {

    private String type;





    private webapp_Mapping webapp_mapping;




    private webapp_Action webapp_action;




    private webapp_Mapping webapp_mapping;




    private webapp_Validator webapp_validator;


    public webapp_Input(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public webapp_Mapping getWebapp_mapping() {
        return webapp_mapping;
    }

    public void setWebapp_mapping(webapp_Mapping webapp_mapping) {
        this.webapp_mapping = webapp_mapping;
    }
    public webapp_Action getWebapp_action() {
        return webapp_action;
    }

    public void setWebapp_action(webapp_Action webapp_action) {
        this.webapp_action = webapp_action;
    }
    public webapp_Mapping getWebapp_mapping() {
        return webapp_mapping;
    }

    public void setWebapp_mapping(webapp_Mapping webapp_mapping) {
        this.webapp_mapping = webapp_mapping;
    }
    public webapp_Validator getWebapp_validator() {
        return webapp_validator;
    }

    public void setWebapp_validator(webapp_Validator webapp_validator) {
        this.webapp_validator = webapp_validator;
    }

}
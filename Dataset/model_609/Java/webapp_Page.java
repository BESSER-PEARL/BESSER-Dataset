





import java.util.List;
import java.util.ArrayList;

public class webapp_Page  {

    private boolean isMain;
    private String name;





    private webapp_Mapping webapp_mapping;




    private webapp_View webapp_view;




    private webapp_Validator webapp_validator;




    private List<webapp_Properties> webapp_propertiess;


    public webapp_Page(
        boolean isMain,        String name    ) {
        this.isMain = isMain;
        this.name = name;
        this.webapp_propertiess = new ArrayList<>();
    }

    public webapp_Page(
        boolean isMain,        String name        ArrayList<webapp_Properties> webapp_propertiess    ) {
        this.isMain = isMain;
        this.name = name;
        this.webapp_propertiess = webapp_propertiess;
    }

    public boolean getIsmain() {
        return isMain;
    }

    public void setIsmain(boolean isMain) {
        this.isMain = isMain;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public webapp_Mapping getWebapp_mapping() {
        return webapp_mapping;
    }

    public void setWebapp_mapping(webapp_Mapping webapp_mapping) {
        this.webapp_mapping = webapp_mapping;
    }
    public webapp_View getWebapp_view() {
        return webapp_view;
    }

    public void setWebapp_view(webapp_View webapp_view) {
        this.webapp_view = webapp_view;
    }
    public webapp_Validator getWebapp_validator() {
        return webapp_validator;
    }

    public void setWebapp_validator(webapp_Validator webapp_validator) {
        this.webapp_validator = webapp_validator;
    }
    public List<webapp_Properties> getWebapp_propertiess() {
        return webapp_propertiess;
    }

    public void addWebapp_properties(Webapp_properties webapp_properties) {
        this.webapp_propertiess.add(webapp_properties);
    }

}
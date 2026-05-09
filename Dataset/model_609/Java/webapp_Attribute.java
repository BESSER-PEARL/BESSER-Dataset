





import java.util.List;
import java.util.ArrayList;

public class webapp_Attribute  {

    private String name;
    private String value;





    private webapp_Tag webapp_tag;


    public webapp_Attribute(
        String name,        String value    ) {
        this.name = name;
        this.value = value;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public webapp_Tag getWebapp_tag() {
        return webapp_tag;
    }

    public void setWebapp_tag(webapp_Tag webapp_tag) {
        this.webapp_tag = webapp_tag;
    }

}
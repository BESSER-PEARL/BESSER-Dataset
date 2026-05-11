





import java.util.List;
import java.util.ArrayList;

public class webapp_UIElement extends Named {

    private String type;





    private webapp_DataStructure webapp_datastructure;


    public webapp_UIElement(
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

    public webapp_DataStructure getWebapp_datastructure() {
        return webapp_datastructure;
    }

    public void setWebapp_datastructure(webapp_DataStructure webapp_datastructure) {
        this.webapp_datastructure = webapp_datastructure;
    }

}
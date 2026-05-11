





import java.util.List;
import java.util.ArrayList;

public class webGui_Feature  {

    private String name;
    private boolean multivalued;





    private webGui_Entity webgui_entity;




    private webGui_Type webgui_type;


    public webGui_Feature(
        String name,        boolean multivalued    ) {
        this.name = name;
        this.multivalued = multivalued;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getMultivalued() {
        return multivalued;
    }

    public void setMultivalued(boolean multivalued) {
        this.multivalued = multivalued;
    }

    public webGui_Entity getWebgui_entity() {
        return webgui_entity;
    }

    public void setWebgui_entity(webGui_Entity webgui_entity) {
        this.webgui_entity = webgui_entity;
    }
    public webGui_Type getWebgui_type() {
        return webgui_type;
    }

    public void setWebgui_type(webGui_Type webgui_type) {
        this.webgui_type = webgui_type;
    }

}
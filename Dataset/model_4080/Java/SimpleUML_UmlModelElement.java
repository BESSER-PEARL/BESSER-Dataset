





import java.util.List;
import java.util.ArrayList;

public class SimpleUML_UmlModelElement  {

    private String umlName;
    private String umlKind;
    private String id;



    public SimpleUML_UmlModelElement(
        String umlName,        String umlKind,        String id    ) {
        this.umlName = umlName;
        this.umlKind = umlKind;
        this.id = id;
    }


    public String getUmlname() {
        return umlName;
    }

    public void setUmlname(String umlName) {
        this.umlName = umlName;
    }
    public String getUmlkind() {
        return umlKind;
    }

    public void setUmlkind(String umlKind) {
        this.umlKind = umlKind;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}
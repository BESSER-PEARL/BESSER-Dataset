





import java.util.List;
import java.util.ArrayList;

public class SimpleUML_UmlModelElement  {

    private String id;
    private String umlName;
    private String umlKind;



    public SimpleUML_UmlModelElement(
        String id,        String umlName,        String umlKind    ) {
        this.id = id;
        this.umlName = umlName;
        this.umlKind = umlKind;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
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


}
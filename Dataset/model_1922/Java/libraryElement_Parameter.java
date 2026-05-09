





import java.util.List;
import java.util.ArrayList;

public class libraryElement_Parameter  {

    private String value;
    private String name;
    private String comment;





    private libraryElement_ConfigurableObject libraryelement_configurableobject;


    public libraryElement_Parameter(
        String value,        String name,        String comment    ) {
        this.value = value;
        this.name = name;
        this.comment = comment;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    public libraryElement_ConfigurableObject getLibraryelement_configurableobject() {
        return libraryelement_configurableobject;
    }

    public void setLibraryelement_configurableobject(libraryElement_ConfigurableObject libraryelement_configurableobject) {
        this.libraryelement_configurableobject = libraryelement_configurableobject;
    }

}
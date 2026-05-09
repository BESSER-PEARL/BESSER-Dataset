





import java.util.List;
import java.util.ArrayList;

public class Docbook_ParaType  {

    private String group;
    private String mixed;
    private String id;
    private String role;





    private Docbook_AbstractType docbook_abstracttype;


    public Docbook_ParaType(
        String group,        String mixed,        String id,        String role    ) {
        this.group = group;
        this.mixed = mixed;
        this.id = id;
        this.role = role;
    }


    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getRole() {
        return role;
    }

    public void setRole(String role) {
        this.role = role;
    }

    public Docbook_AbstractType getDocbook_abstracttype() {
        return docbook_abstracttype;
    }

    public void setDocbook_abstracttype(Docbook_AbstractType docbook_abstracttype) {
        this.docbook_abstracttype = docbook_abstracttype;
    }

}
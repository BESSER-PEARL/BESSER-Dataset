





import java.util.List;
import java.util.ArrayList;

public class express_core_Remark  {

    private String isTail;
    private String text;
    private String isTagged;





    private List<Schema> schemas;




    private List<NamedElement> namedelements;




    private Scope scope;


    public express_core_Remark(
        String isTail,        String text,        String isTagged    ) {
        this.isTail = isTail;
        this.text = text;
        this.isTagged = isTagged;
        this.schemas = new ArrayList<>();
        this.namedelements = new ArrayList<>();
    }

    public express_core_Remark(
        String isTail,        String text,        String isTagged        ArrayList<Schema> schemas,        ArrayList<NamedElement> namedelements    ) {
        this.isTail = isTail;
        this.text = text;
        this.isTagged = isTagged;
        this.schemas = schemas;
        this.namedelements = namedelements;
    }

    public String getIstail() {
        return isTail;
    }

    public void setIstail(String isTail) {
        this.isTail = isTail;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getIstagged() {
        return isTagged;
    }

    public void setIstagged(String isTagged) {
        this.isTagged = isTagged;
    }

    public List<Schema> getSchemas() {
        return schemas;
    }

    public void addSchema(Schema schema) {
        this.schemas.add(schema);
    }
    public List<NamedElement> getNamedelements() {
        return namedelements;
    }

    public void addNamedelement(Namedelement namedelement) {
        this.namedelements.add(namedelement);
    }
    public Scope getScope() {
        return scope;
    }

    public void setScope(Scope scope) {
        this.scope = scope;
    }

}
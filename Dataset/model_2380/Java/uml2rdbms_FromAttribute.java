





import java.util.List;
import java.util.ArrayList;

public class uml2rdbms_FromAttribute  {

    private String kind;
    private String name;





    private List<uml2rdbms_AttributeToColumn> uml2rdbms_attributetocolumns;


    public uml2rdbms_FromAttribute(
        String kind,        String name    ) {
        this.kind = kind;
        this.name = name;
        this.uml2rdbms_attributetocolumns = new ArrayList<>();
    }

    public uml2rdbms_FromAttribute(
        String kind,        String name        ArrayList<uml2rdbms_AttributeToColumn> uml2rdbms_attributetocolumns    ) {
        this.kind = kind;
        this.name = name;
        this.uml2rdbms_attributetocolumns = uml2rdbms_attributetocolumns;
    }

    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<uml2rdbms_AttributeToColumn> getUml2rdbms_attributetocolumns() {
        return uml2rdbms_attributetocolumns;
    }

    public void addUml2rdbms_attributetocolumn(Uml2rdbms_attributetocolumn uml2rdbms_attributetocolumn) {
        this.uml2rdbms_attributetocolumns.add(uml2rdbms_attributetocolumn);
    }

}
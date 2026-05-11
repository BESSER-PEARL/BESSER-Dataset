





import java.util.List;
import java.util.ArrayList;

public class uml2rdbms_FromAttribute  {

    private String kind;
    private String name;





    private uml2rdbms_FromAttributeOwner uml2rdbms_fromattributeowner;




    private uml2rdbms_FromAttributeOwner uml2rdbms_fromattributeowner;




    private List<uml2rdbms_AttributeToColumn> uml2rdbms_attributetocolumns;




    private uml2rdbms_Attribute uml2rdbms_attribute;


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

    public uml2rdbms_FromAttributeOwner getUml2rdbms_fromattributeowner() {
        return uml2rdbms_fromattributeowner;
    }

    public void setUml2rdbms_fromattributeowner(uml2rdbms_FromAttributeOwner uml2rdbms_fromattributeowner) {
        this.uml2rdbms_fromattributeowner = uml2rdbms_fromattributeowner;
    }
    public uml2rdbms_FromAttributeOwner getUml2rdbms_fromattributeowner() {
        return uml2rdbms_fromattributeowner;
    }

    public void setUml2rdbms_fromattributeowner(uml2rdbms_FromAttributeOwner uml2rdbms_fromattributeowner) {
        this.uml2rdbms_fromattributeowner = uml2rdbms_fromattributeowner;
    }
    public List<uml2rdbms_AttributeToColumn> getUml2rdbms_attributetocolumns() {
        return uml2rdbms_attributetocolumns;
    }

    public void addUml2rdbms_attributetocolumn(Uml2rdbms_attributetocolumn uml2rdbms_attributetocolumn) {
        this.uml2rdbms_attributetocolumns.add(uml2rdbms_attributetocolumn);
    }
    public uml2rdbms_Attribute getUml2rdbms_attribute() {
        return uml2rdbms_attribute;
    }

    public void setUml2rdbms_attribute(uml2rdbms_Attribute uml2rdbms_attribute) {
        this.uml2rdbms_attribute = uml2rdbms_attribute;
    }

}
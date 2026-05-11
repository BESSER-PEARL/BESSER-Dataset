





import java.util.List;
import java.util.ArrayList;

public class uml2rdbms_PrimitiveToName  {

    private String typeName;
    private String name;





    private uml2rdbms_AttributeToColumn uml2rdbms_attributetocolumn;


    public uml2rdbms_PrimitiveToName(
        String typeName,        String name    ) {
        this.typeName = typeName;
        this.name = name;
    }


    public String getTypename() {
        return typeName;
    }

    public void setTypename(String typeName) {
        this.typeName = typeName;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public uml2rdbms_AttributeToColumn getUml2rdbms_attributetocolumn() {
        return uml2rdbms_attributetocolumn;
    }

    public void setUml2rdbms_attributetocolumn(uml2rdbms_AttributeToColumn uml2rdbms_attributetocolumn) {
        this.uml2rdbms_attributetocolumn = uml2rdbms_attributetocolumn;
    }

}
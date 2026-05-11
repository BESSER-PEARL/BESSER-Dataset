





import java.util.List;
import java.util.ArrayList;

public class umltordbms_PrimitiveToName  {

    private String name;
    private String typeName;





    private umltordbms_AttributeToColumn umltordbms_attributetocolumn;


    public umltordbms_PrimitiveToName(
        String name,        String typeName    ) {
        this.name = name;
        this.typeName = typeName;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTypename() {
        return typeName;
    }

    public void setTypename(String typeName) {
        this.typeName = typeName;
    }

    public umltordbms_AttributeToColumn getUmltordbms_attributetocolumn() {
        return umltordbms_attributetocolumn;
    }

    public void setUmltordbms_attributetocolumn(umltordbms_AttributeToColumn umltordbms_attributetocolumn) {
        this.umltordbms_attributetocolumn = umltordbms_attributetocolumn;
    }

}
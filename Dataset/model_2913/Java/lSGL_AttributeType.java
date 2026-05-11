





import java.util.List;
import java.util.ArrayList;

public class lSGL_AttributeType  {

    private boolean nullable;
    private String typeName;





    private lSGL_Attribute lsgl_attribute;




    private lSGL_Attribute lsgl_attribute;


    public lSGL_AttributeType(
        boolean nullable,        String typeName    ) {
        this.nullable = nullable;
        this.typeName = typeName;
    }


    public boolean getNullable() {
        return nullable;
    }

    public void setNullable(boolean nullable) {
        this.nullable = nullable;
    }
    public String getTypename() {
        return typeName;
    }

    public void setTypename(String typeName) {
        this.typeName = typeName;
    }

    public lSGL_Attribute getLsgl_attribute() {
        return lsgl_attribute;
    }

    public void setLsgl_attribute(lSGL_Attribute lsgl_attribute) {
        this.lsgl_attribute = lsgl_attribute;
    }
    public lSGL_Attribute getLsgl_attribute() {
        return lsgl_attribute;
    }

    public void setLsgl_attribute(lSGL_Attribute lsgl_attribute) {
        this.lsgl_attribute = lsgl_attribute;
    }

}
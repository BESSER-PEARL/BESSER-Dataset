





import java.util.List;
import java.util.ArrayList;

public class xpdl_BasicTypeType extends XpdlTypeType {

    private String type;





    private xpdl_DataTypeType xpdl_datatypetype;


    public xpdl_BasicTypeType(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public xpdl_DataTypeType getXpdl_datatypetype() {
        return xpdl_datatypetype;
    }

    public void setXpdl_datatypetype(xpdl_DataTypeType xpdl_datatypetype) {
        this.xpdl_datatypetype = xpdl_datatypetype;
    }

}
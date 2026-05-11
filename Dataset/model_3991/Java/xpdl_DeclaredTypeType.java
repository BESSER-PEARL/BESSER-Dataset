





import java.util.List;
import java.util.ArrayList;

public class xpdl_DeclaredTypeType extends XpdlTypeType {

    private String id;





    private xpdl_DataTypeType xpdl_datatypetype;


    public xpdl_DeclaredTypeType(
        String id    ) {
        super(
        );
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public xpdl_DataTypeType getXpdl_datatypetype() {
        return xpdl_datatypetype;
    }

    public void setXpdl_datatypetype(xpdl_DataTypeType xpdl_datatypetype) {
        this.xpdl_datatypetype = xpdl_datatypetype;
    }

}
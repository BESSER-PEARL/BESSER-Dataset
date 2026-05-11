





import java.util.List;
import java.util.ArrayList;

public class xpdl2_FormalParameterType  {

    private String name;
    private String description;
    private String id;
    private String mode;





    private xpdl2_DataTypeType xpdl2_datatypetype;


    public xpdl2_FormalParameterType(
        String name,        String description,        String id,        String mode    ) {
        this.name = name;
        this.description = description;
        this.id = id;
        this.mode = mode;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getMode() {
        return mode;
    }

    public void setMode(String mode) {
        this.mode = mode;
    }

    public xpdl2_DataTypeType getXpdl2_datatypetype() {
        return xpdl2_datatypetype;
    }

    public void setXpdl2_datatypetype(xpdl2_DataTypeType xpdl2_datatypetype) {
        this.xpdl2_datatypetype = xpdl2_datatypetype;
    }

}
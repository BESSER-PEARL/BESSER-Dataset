





import java.util.List;
import java.util.ArrayList;

public class xpdl_FormalParameterType  {

    private String description;
    private String mode;
    private String id;
    private String name;





    private xpdl_DataTypeType xpdl_datatypetype;




    private xpdl_FormalParametersType xpdl_formalparameterstype;


    public xpdl_FormalParameterType(
        String description,        String mode,        String id,        String name    ) {
        this.description = description;
        this.mode = mode;
        this.id = id;
        this.name = name;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getMode() {
        return mode;
    }

    public void setMode(String mode) {
        this.mode = mode;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public xpdl_DataTypeType getXpdl_datatypetype() {
        return xpdl_datatypetype;
    }

    public void setXpdl_datatypetype(xpdl_DataTypeType xpdl_datatypetype) {
        this.xpdl_datatypetype = xpdl_datatypetype;
    }
    public xpdl_FormalParametersType getXpdl_formalparameterstype() {
        return xpdl_formalparameterstype;
    }

    public void setXpdl_formalparameterstype(xpdl_FormalParametersType xpdl_formalparameterstype) {
        this.xpdl_formalparameterstype = xpdl_formalparameterstype;
    }

}
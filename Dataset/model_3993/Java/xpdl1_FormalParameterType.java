





import java.util.List;
import java.util.ArrayList;

public class xpdl1_FormalParameterType  {

    private String mode;
    private String index;
    private String id;
    private String description;





    private xpdl1_DocumentRoot xpdl1_documentroot;




    private xpdl1_FormalParametersType xpdl1_formalparameterstype;




    private xpdl1_DataTypeType xpdl1_datatypetype;


    public xpdl1_FormalParameterType(
        String mode,        String index,        String id,        String description    ) {
        this.mode = mode;
        this.index = index;
        this.id = id;
        this.description = description;
    }


    public String getMode() {
        return mode;
    }

    public void setMode(String mode) {
        this.mode = mode;
    }
    public String getIndex() {
        return index;
    }

    public void setIndex(String index) {
        this.index = index;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public xpdl1_DocumentRoot getXpdl1_documentroot() {
        return xpdl1_documentroot;
    }

    public void setXpdl1_documentroot(xpdl1_DocumentRoot xpdl1_documentroot) {
        this.xpdl1_documentroot = xpdl1_documentroot;
    }
    public xpdl1_FormalParametersType getXpdl1_formalparameterstype() {
        return xpdl1_formalparameterstype;
    }

    public void setXpdl1_formalparameterstype(xpdl1_FormalParametersType xpdl1_formalparameterstype) {
        this.xpdl1_formalparameterstype = xpdl1_formalparameterstype;
    }
    public xpdl1_DataTypeType getXpdl1_datatypetype() {
        return xpdl1_datatypetype;
    }

    public void setXpdl1_datatypetype(xpdl1_DataTypeType xpdl1_datatypetype) {
        this.xpdl1_datatypetype = xpdl1_datatypetype;
    }

}
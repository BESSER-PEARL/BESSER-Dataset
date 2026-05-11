





import java.util.List;
import java.util.ArrayList;

public class jpdl32_VariableType  {

    private String name;
    private String any;
    private String mappedName;
    private String access;





    private jpdl32_ProcessStateType jpdl32_processstatetype;




    private jpdl32_DocumentRoot jpdl32_documentroot;


    public jpdl32_VariableType(
        String name,        String any,        String mappedName,        String access    ) {
        this.name = name;
        this.any = any;
        this.mappedName = mappedName;
        this.access = access;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAny() {
        return any;
    }

    public void setAny(String any) {
        this.any = any;
    }
    public String getMappedname() {
        return mappedName;
    }

    public void setMappedname(String mappedName) {
        this.mappedName = mappedName;
    }
    public String getAccess() {
        return access;
    }

    public void setAccess(String access) {
        this.access = access;
    }

    public jpdl32_ProcessStateType getJpdl32_processstatetype() {
        return jpdl32_processstatetype;
    }

    public void setJpdl32_processstatetype(jpdl32_ProcessStateType jpdl32_processstatetype) {
        this.jpdl32_processstatetype = jpdl32_processstatetype;
    }
    public jpdl32_DocumentRoot getJpdl32_documentroot() {
        return jpdl32_documentroot;
    }

    public void setJpdl32_documentroot(jpdl32_DocumentRoot jpdl32_documentroot) {
        this.jpdl32_documentroot = jpdl32_documentroot;
    }

}






import java.util.List;
import java.util.ArrayList;

public class jpdl31_VariableType  {

    private String access;
    private String name;
    private String any;
    private String mappedName;





    private jpdl31_ProcessStateType jpdl31_processstatetype;




    private jpdl31_DocumentRoot jpdl31_documentroot;


    public jpdl31_VariableType(
        String access,        String name,        String any,        String mappedName    ) {
        this.access = access;
        this.name = name;
        this.any = any;
        this.mappedName = mappedName;
    }


    public String getAccess() {
        return access;
    }

    public void setAccess(String access) {
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

    public jpdl31_ProcessStateType getJpdl31_processstatetype() {
        return jpdl31_processstatetype;
    }

    public void setJpdl31_processstatetype(jpdl31_ProcessStateType jpdl31_processstatetype) {
        this.jpdl31_processstatetype = jpdl31_processstatetype;
    }
    public jpdl31_DocumentRoot getJpdl31_documentroot() {
        return jpdl31_documentroot;
    }

    public void setJpdl31_documentroot(jpdl31_DocumentRoot jpdl31_documentroot) {
        this.jpdl31_documentroot = jpdl31_documentroot;
    }

}
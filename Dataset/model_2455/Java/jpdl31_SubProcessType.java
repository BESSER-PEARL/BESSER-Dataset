





import java.util.List;
import java.util.ArrayList;

public class jpdl31_SubProcessType  {

    private String version;
    private String name;





    private jpdl31_ProcessStateType jpdl31_processstatetype;


    public jpdl31_SubProcessType(
        String version,        String name    ) {
        this.version = version;
        this.name = name;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public jpdl31_ProcessStateType getJpdl31_processstatetype() {
        return jpdl31_processstatetype;
    }

    public void setJpdl31_processstatetype(jpdl31_ProcessStateType jpdl31_processstatetype) {
        this.jpdl31_processstatetype = jpdl31_processstatetype;
    }

}
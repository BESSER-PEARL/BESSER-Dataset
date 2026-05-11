





import java.util.List;
import java.util.ArrayList;

public class jpdl32_SubProcessType  {

    private String version;
    private String binding;
    private String name;





    private jpdl32_ProcessStateType jpdl32_processstatetype;


    public jpdl32_SubProcessType(
        String version,        String binding,        String name    ) {
        this.version = version;
        this.binding = binding;
        this.name = name;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getBinding() {
        return binding;
    }

    public void setBinding(String binding) {
        this.binding = binding;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public jpdl32_ProcessStateType getJpdl32_processstatetype() {
        return jpdl32_processstatetype;
    }

    public void setJpdl32_processstatetype(jpdl32_ProcessStateType jpdl32_processstatetype) {
        this.jpdl32_processstatetype = jpdl32_processstatetype;
    }

}
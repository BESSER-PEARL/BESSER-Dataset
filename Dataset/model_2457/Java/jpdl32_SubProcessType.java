





import java.util.List;
import java.util.ArrayList;

public class jpdl32_SubProcessType  {

    private String version;
    private String name;
    private String binding;





    private jpdl32_ProcessStateType jpdl32_processstatetype;


    public jpdl32_SubProcessType(
        String version,        String name,        String binding    ) {
        this.version = version;
        this.name = name;
        this.binding = binding;
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
    public String getBinding() {
        return binding;
    }

    public void setBinding(String binding) {
        this.binding = binding;
    }

    public jpdl32_ProcessStateType getJpdl32_processstatetype() {
        return jpdl32_processstatetype;
    }

    public void setJpdl32_processstatetype(jpdl32_ProcessStateType jpdl32_processstatetype) {
        this.jpdl32_processstatetype = jpdl32_processstatetype;
    }

}
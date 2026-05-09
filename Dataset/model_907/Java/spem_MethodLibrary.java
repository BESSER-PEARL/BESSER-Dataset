





import java.util.List;
import java.util.ArrayList;

public class spem_MethodLibrary  {

    private String name;





    private List<spem_MethodConfiguration> spem_methodconfigurations;




    private spem_ToolDefinition spem_tooldefinition;




    private List<spem_MethodPlugin> spem_methodplugins;


    public spem_MethodLibrary(
        String name    ) {
        this.name = name;
        this.spem_methodconfigurations = new ArrayList<>();
        this.spem_methodplugins = new ArrayList<>();
    }

    public spem_MethodLibrary(
        String name        ArrayList<spem_MethodConfiguration> spem_methodconfigurations,        ArrayList<spem_MethodPlugin> spem_methodplugins    ) {
        this.name = name;
        this.spem_methodconfigurations = spem_methodconfigurations;
        this.spem_methodplugins = spem_methodplugins;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<spem_MethodConfiguration> getSpem_methodconfigurations() {
        return spem_methodconfigurations;
    }

    public void addSpem_methodconfiguration(Spem_methodconfiguration spem_methodconfiguration) {
        this.spem_methodconfigurations.add(spem_methodconfiguration);
    }
    public spem_ToolDefinition getSpem_tooldefinition() {
        return spem_tooldefinition;
    }

    public void setSpem_tooldefinition(spem_ToolDefinition spem_tooldefinition) {
        this.spem_tooldefinition = spem_tooldefinition;
    }
    public List<spem_MethodPlugin> getSpem_methodplugins() {
        return spem_methodplugins;
    }

    public void addSpem_methodplugin(Spem_methodplugin spem_methodplugin) {
        this.spem_methodplugins.add(spem_methodplugin);
    }

}
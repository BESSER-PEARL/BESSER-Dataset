





import java.util.List;
import java.util.ArrayList;

public class spem_MethodLibrary  {

    private String name;





    private List<spem_MethodConfiguration> spem_methodconfigurations;




    private List<spem_MethodPlugin> spem_methodplugins;




    private spem_MethodContentPackage spem_methodcontentpackage;


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
    public List<spem_MethodPlugin> getSpem_methodplugins() {
        return spem_methodplugins;
    }

    public void addSpem_methodplugin(Spem_methodplugin spem_methodplugin) {
        this.spem_methodplugins.add(spem_methodplugin);
    }
    public spem_MethodContentPackage getSpem_methodcontentpackage() {
        return spem_methodcontentpackage;
    }

    public void setSpem_methodcontentpackage(spem_MethodContentPackage spem_methodcontentpackage) {
        this.spem_methodcontentpackage = spem_methodcontentpackage;
    }

}
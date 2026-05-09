





import java.util.List;
import java.util.ArrayList;

public class spem_MethodPlugin extends MethodLibraryPackageableElement {






    private spem_MethodConfiguration spem_methodconfiguration;




    private List<spem_ProcessPackage> spem_processpackages;




    private spem_MethodPlugin spem_methodplugin;




    private List<spem_MethodContentPackage> spem_methodcontentpackages;


    public spem_MethodPlugin(
    ) {
        super(
        );
        this.spem_processpackages = new ArrayList<>();
        this.spem_methodcontentpackages = new ArrayList<>();
    }

    public spem_MethodPlugin(
        ArrayList<spem_ProcessPackage> spem_processpackages,        ArrayList<spem_MethodContentPackage> spem_methodcontentpackages    ) {
        this.spem_processpackages = spem_processpackages;
        this.spem_methodcontentpackages = spem_methodcontentpackages;
    }


    public spem_MethodConfiguration getSpem_methodconfiguration() {
        return spem_methodconfiguration;
    }

    public void setSpem_methodconfiguration(spem_MethodConfiguration spem_methodconfiguration) {
        this.spem_methodconfiguration = spem_methodconfiguration;
    }
    public List<spem_ProcessPackage> getSpem_processpackages() {
        return spem_processpackages;
    }

    public void addSpem_processpackage(Spem_processpackage spem_processpackage) {
        this.spem_processpackages.add(spem_processpackage);
    }
    public spem_MethodPlugin getSpem_methodplugin() {
        return spem_methodplugin;
    }

    public void setSpem_methodplugin(spem_MethodPlugin spem_methodplugin) {
        this.spem_methodplugin = spem_methodplugin;
    }
    public List<spem_MethodContentPackage> getSpem_methodcontentpackages() {
        return spem_methodcontentpackages;
    }

    public void addSpem_methodcontentpackage(Spem_methodcontentpackage spem_methodcontentpackage) {
        this.spem_methodcontentpackages.add(spem_methodcontentpackage);
    }

}
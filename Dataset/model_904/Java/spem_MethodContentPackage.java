





import java.util.List;
import java.util.ArrayList;

public class spem_MethodContentPackage extends MethodPluginPackageableElement, MethodContentPackageableElement {






    private spem_MethodConfiguration spem_methodconfiguration;




    private List<spem_MethodContentPackage> spem_methodcontentpackages;


    public spem_MethodContentPackage(
    ) {
        super(
        );
        this.spem_methodcontentpackages = new ArrayList<>();
    }

    public spem_MethodContentPackage(
        ArrayList<spem_MethodContentPackage> spem_methodcontentpackages    ) {
        this.spem_methodcontentpackages = spem_methodcontentpackages;
    }


    public spem_MethodConfiguration getSpem_methodconfiguration() {
        return spem_methodconfiguration;
    }

    public void setSpem_methodconfiguration(spem_MethodConfiguration spem_methodconfiguration) {
        this.spem_methodconfiguration = spem_methodconfiguration;
    }
    public List<spem_MethodContentPackage> getSpem_methodcontentpackages() {
        return spem_methodcontentpackages;
    }

    public void addSpem_methodcontentpackage(Spem_methodcontentpackage spem_methodcontentpackage) {
        this.spem_methodcontentpackages.add(spem_methodcontentpackage);
    }

}
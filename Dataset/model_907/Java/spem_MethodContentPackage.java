





import java.util.List;
import java.util.ArrayList;

public class spem_MethodContentPackage extends MethodPluginPackageableElement, MethodContentPackageableElement {






    private spem_MethodConfiguration spem_methodconfiguration;




    private spem_MethodContentPackage spem_methodcontentpackage;




    private List<spem_MethodContentPackageableElement> spem_methodcontentpackageableelements;


    public spem_MethodContentPackage(
    ) {
        super(
        );
        this.spem_methodcontentpackageableelements = new ArrayList<>();
    }

    public spem_MethodContentPackage(
        ArrayList<spem_MethodContentPackageableElement> spem_methodcontentpackageableelements    ) {
        this.spem_methodcontentpackageableelements = spem_methodcontentpackageableelements;
    }


    public spem_MethodConfiguration getSpem_methodconfiguration() {
        return spem_methodconfiguration;
    }

    public void setSpem_methodconfiguration(spem_MethodConfiguration spem_methodconfiguration) {
        this.spem_methodconfiguration = spem_methodconfiguration;
    }
    public spem_MethodContentPackage getSpem_methodcontentpackage() {
        return spem_methodcontentpackage;
    }

    public void setSpem_methodcontentpackage(spem_MethodContentPackage spem_methodcontentpackage) {
        this.spem_methodcontentpackage = spem_methodcontentpackage;
    }
    public List<spem_MethodContentPackageableElement> getSpem_methodcontentpackageableelements() {
        return spem_methodcontentpackageableelements;
    }

    public void addSpem_methodcontentpackageableelement(Spem_methodcontentpackageableelement spem_methodcontentpackageableelement) {
        this.spem_methodcontentpackageableelements.add(spem_methodcontentpackageableelement);
    }

}
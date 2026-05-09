





import java.util.List;
import java.util.ArrayList;

public class spem_MethodPlugin extends MethodLibraryPackageableElement {

    private boolean userChangeable;
    private String supporting;





    private spem_MethodConfiguration spem_methodconfiguration;




    private List<spem_MethodPlugin> spem_methodplugins;




    private List<spem_MethodContentPackage> spem_methodcontentpackages;




    private List<spem_MethodPlugin> spem_methodplugins;




    private List<spem_ProcessPackage> spem_processpackages;


    public spem_MethodPlugin(
        boolean userChangeable,        String supporting    ) {
        super(
        );
        this.userChangeable = userChangeable;
        this.supporting = supporting;
        this.spem_methodplugins = new ArrayList<>();
        this.spem_methodcontentpackages = new ArrayList<>();
        this.spem_methodplugins = new ArrayList<>();
        this.spem_processpackages = new ArrayList<>();
    }

    public spem_MethodPlugin(
        boolean userChangeable,        String supporting        ArrayList<spem_MethodPlugin> spem_methodplugins,        ArrayList<spem_MethodContentPackage> spem_methodcontentpackages,        ArrayList<spem_MethodPlugin> spem_methodplugins,        ArrayList<spem_ProcessPackage> spem_processpackages    ) {
        this.userChangeable = userChangeable;
        this.supporting = supporting;
        this.spem_methodplugins = spem_methodplugins;
        this.spem_methodcontentpackages = spem_methodcontentpackages;
        this.spem_methodplugins = spem_methodplugins;
        this.spem_processpackages = spem_processpackages;
    }

    public boolean getUserchangeable() {
        return userChangeable;
    }

    public void setUserchangeable(boolean userChangeable) {
        this.userChangeable = userChangeable;
    }
    public String getSupporting() {
        return supporting;
    }

    public void setSupporting(String supporting) {
        this.supporting = supporting;
    }

    public spem_MethodConfiguration getSpem_methodconfiguration() {
        return spem_methodconfiguration;
    }

    public void setSpem_methodconfiguration(spem_MethodConfiguration spem_methodconfiguration) {
        this.spem_methodconfiguration = spem_methodconfiguration;
    }
    public List<spem_MethodPlugin> getSpem_methodplugins() {
        return spem_methodplugins;
    }

    public void addSpem_methodplugin(Spem_methodplugin spem_methodplugin) {
        this.spem_methodplugins.add(spem_methodplugin);
    }
    public List<spem_MethodContentPackage> getSpem_methodcontentpackages() {
        return spem_methodcontentpackages;
    }

    public void addSpem_methodcontentpackage(Spem_methodcontentpackage spem_methodcontentpackage) {
        this.spem_methodcontentpackages.add(spem_methodcontentpackage);
    }
    public List<spem_MethodPlugin> getSpem_methodplugins() {
        return spem_methodplugins;
    }

    public void addSpem_methodplugin(Spem_methodplugin spem_methodplugin) {
        this.spem_methodplugins.add(spem_methodplugin);
    }
    public List<spem_ProcessPackage> getSpem_processpackages() {
        return spem_processpackages;
    }

    public void addSpem_processpackage(Spem_processpackage spem_processpackage) {
        this.spem_processpackages.add(spem_processpackage);
    }

}
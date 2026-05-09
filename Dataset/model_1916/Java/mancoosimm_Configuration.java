





import java.util.List;
import java.util.ArrayList;

public class mancoosimm_Configuration extends NamedElement {

    private String systemType;
    private String creationTime;





    private List<mancoosimm_HalfInstalledPackage> mancoosimm_halfinstalledpackages;




    private mancoosimm_Package mancoosimm_package;


    public mancoosimm_Configuration(
        String systemType,        String creationTime    ) {
        super(
        );
        this.systemType = systemType;
        this.creationTime = creationTime;
        this.mancoosimm_halfinstalledpackages = new ArrayList<>();
    }

    public mancoosimm_Configuration(
        String systemType,        String creationTime        ArrayList<mancoosimm_HalfInstalledPackage> mancoosimm_halfinstalledpackages    ) {
        this.systemType = systemType;
        this.creationTime = creationTime;
        this.mancoosimm_halfinstalledpackages = mancoosimm_halfinstalledpackages;
    }

    public String getSystemtype() {
        return systemType;
    }

    public void setSystemtype(String systemType) {
        this.systemType = systemType;
    }
    public String getCreationtime() {
        return creationTime;
    }

    public void setCreationtime(String creationTime) {
        this.creationTime = creationTime;
    }

    public List<mancoosimm_HalfInstalledPackage> getMancoosimm_halfinstalledpackages() {
        return mancoosimm_halfinstalledpackages;
    }

    public void addMancoosimm_halfinstalledpackage(Mancoosimm_halfinstalledpackage mancoosimm_halfinstalledpackage) {
        this.mancoosimm_halfinstalledpackages.add(mancoosimm_halfinstalledpackage);
    }
    public mancoosimm_Package getMancoosimm_package() {
        return mancoosimm_package;
    }

    public void setMancoosimm_package(mancoosimm_Package mancoosimm_package) {
        this.mancoosimm_package = mancoosimm_package;
    }

}
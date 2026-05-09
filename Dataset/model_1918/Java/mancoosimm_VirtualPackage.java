





import java.util.List;
import java.util.ArrayList;

public class mancoosimm_VirtualPackage extends InstalledPackage {






    private List<mancoosimm_InstalledPackage> mancoosimm_installedpackages;




    private mancoosimm_InstalledPackage mancoosimm_installedpackage;


    public mancoosimm_VirtualPackage(
    ) {
        super(
        );
        this.mancoosimm_installedpackages = new ArrayList<>();
    }

    public mancoosimm_VirtualPackage(
        ArrayList<mancoosimm_InstalledPackage> mancoosimm_installedpackages    ) {
        this.mancoosimm_installedpackages = mancoosimm_installedpackages;
    }


    public List<mancoosimm_InstalledPackage> getMancoosimm_installedpackages() {
        return mancoosimm_installedpackages;
    }

    public void addMancoosimm_installedpackage(Mancoosimm_installedpackage mancoosimm_installedpackage) {
        this.mancoosimm_installedpackages.add(mancoosimm_installedpackage);
    }
    public mancoosimm_InstalledPackage getMancoosimm_installedpackage() {
        return mancoosimm_installedpackage;
    }

    public void setMancoosimm_installedpackage(mancoosimm_InstalledPackage mancoosimm_installedpackage) {
        this.mancoosimm_installedpackage = mancoosimm_installedpackage;
    }

}
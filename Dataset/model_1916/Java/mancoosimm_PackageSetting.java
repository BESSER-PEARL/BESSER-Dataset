





import java.util.List;
import java.util.ArrayList;

public class mancoosimm_PackageSetting extends NamedElement {






    private mancoosimm_Package mancoosimm_package;




    private mancoosimm_Package mancoosimm_package;




    private List<mancoosimm_Service> mancoosimm_services;




    private List<mancoosimm_PackageSetting> mancoosimm_packagesettings;




    private List<mancoosimm_File> mancoosimm_files;




    private mancoosimm_File mancoosimm_file;


    public mancoosimm_PackageSetting(
    ) {
        super(
        );
        this.mancoosimm_services = new ArrayList<>();
        this.mancoosimm_packagesettings = new ArrayList<>();
        this.mancoosimm_files = new ArrayList<>();
    }

    public mancoosimm_PackageSetting(
        ArrayList<mancoosimm_Service> mancoosimm_services,        ArrayList<mancoosimm_PackageSetting> mancoosimm_packagesettings,        ArrayList<mancoosimm_File> mancoosimm_files    ) {
        this.mancoosimm_services = mancoosimm_services;
        this.mancoosimm_packagesettings = mancoosimm_packagesettings;
        this.mancoosimm_files = mancoosimm_files;
    }


    public mancoosimm_Package getMancoosimm_package() {
        return mancoosimm_package;
    }

    public void setMancoosimm_package(mancoosimm_Package mancoosimm_package) {
        this.mancoosimm_package = mancoosimm_package;
    }
    public mancoosimm_Package getMancoosimm_package() {
        return mancoosimm_package;
    }

    public void setMancoosimm_package(mancoosimm_Package mancoosimm_package) {
        this.mancoosimm_package = mancoosimm_package;
    }
    public List<mancoosimm_Service> getMancoosimm_services() {
        return mancoosimm_services;
    }

    public void addMancoosimm_service(Mancoosimm_service mancoosimm_service) {
        this.mancoosimm_services.add(mancoosimm_service);
    }
    public List<mancoosimm_PackageSetting> getMancoosimm_packagesettings() {
        return mancoosimm_packagesettings;
    }

    public void addMancoosimm_packagesetting(Mancoosimm_packagesetting mancoosimm_packagesetting) {
        this.mancoosimm_packagesettings.add(mancoosimm_packagesetting);
    }
    public List<mancoosimm_File> getMancoosimm_files() {
        return mancoosimm_files;
    }

    public void addMancoosimm_file(Mancoosimm_file mancoosimm_file) {
        this.mancoosimm_files.add(mancoosimm_file);
    }
    public mancoosimm_File getMancoosimm_file() {
        return mancoosimm_file;
    }

    public void setMancoosimm_file(mancoosimm_File mancoosimm_file) {
        this.mancoosimm_file = mancoosimm_file;
    }

}
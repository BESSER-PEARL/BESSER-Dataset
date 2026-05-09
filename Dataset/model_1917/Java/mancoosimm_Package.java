





import java.util.List;
import java.util.ArrayList;

public class mancoosimm_Package extends NamedElement {

    private String architecture;
    private String version;





    private mancoosimm_PackageSetting mancoosimm_packagesetting;




    private mancoosimm_Configuration mancoosimm_configuration;




    private mancoosimm_PackageSetting mancoosimm_packagesetting;


    public mancoosimm_Package(
        String architecture,        String version    ) {
        super(
        );
        this.architecture = architecture;
        this.version = version;
    }


    public String getArchitecture() {
        return architecture;
    }

    public void setArchitecture(String architecture) {
        this.architecture = architecture;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }

    public mancoosimm_PackageSetting getMancoosimm_packagesetting() {
        return mancoosimm_packagesetting;
    }

    public void setMancoosimm_packagesetting(mancoosimm_PackageSetting mancoosimm_packagesetting) {
        this.mancoosimm_packagesetting = mancoosimm_packagesetting;
    }
    public mancoosimm_Configuration getMancoosimm_configuration() {
        return mancoosimm_configuration;
    }

    public void setMancoosimm_configuration(mancoosimm_Configuration mancoosimm_configuration) {
        this.mancoosimm_configuration = mancoosimm_configuration;
    }
    public mancoosimm_PackageSetting getMancoosimm_packagesetting() {
        return mancoosimm_packagesetting;
    }

    public void setMancoosimm_packagesetting(mancoosimm_PackageSetting mancoosimm_packagesetting) {
        this.mancoosimm_packagesetting = mancoosimm_packagesetting;
    }

}
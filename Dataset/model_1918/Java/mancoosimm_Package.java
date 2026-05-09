





import java.util.List;
import java.util.ArrayList;

public class mancoosimm_Package extends NamedElement {

    private String version;
    private String architecture;





    private mancoosimm_Configuration mancoosimm_configuration;




    private mancoosimm_PackageSetting mancoosimm_packagesetting;




    private mancoosimm_PackageSetting mancoosimm_packagesetting;


    public mancoosimm_Package(
        String version,        String architecture    ) {
        super(
        );
        this.version = version;
        this.architecture = architecture;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getArchitecture() {
        return architecture;
    }

    public void setArchitecture(String architecture) {
        this.architecture = architecture;
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
    public mancoosimm_PackageSetting getMancoosimm_packagesetting() {
        return mancoosimm_packagesetting;
    }

    public void setMancoosimm_packagesetting(mancoosimm_PackageSetting mancoosimm_packagesetting) {
        this.mancoosimm_packagesetting = mancoosimm_packagesetting;
    }

}
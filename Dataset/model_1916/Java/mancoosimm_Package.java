





import java.util.List;
import java.util.ArrayList;

public class mancoosimm_Package extends NamedElement {

    private String version;
    private String architecture;



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


}
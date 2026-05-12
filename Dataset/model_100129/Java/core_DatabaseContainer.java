





import java.util.List;
import java.util.ArrayList;

public class core_DatabaseContainer extends ServiceConfig {

    private String version;
    private String vendor;





    private core_CatalogContainer core_catalogcontainer;




    private List<core_CatalogContainer> core_catalogcontainers;


    public core_DatabaseContainer(
        String version,        String vendor    ) {
        super(
        );
        this.version = version;
        this.vendor = vendor;
        this.core_catalogcontainers = new ArrayList<>();
    }

    public core_DatabaseContainer(
        String version,        String vendor        ArrayList<core_CatalogContainer> core_catalogcontainers    ) {
        this.version = version;
        this.vendor = vendor;
        this.core_catalogcontainers = core_catalogcontainers;
    }

    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getVendor() {
        return vendor;
    }

    public void setVendor(String vendor) {
        this.vendor = vendor;
    }

    public core_CatalogContainer getCore_catalogcontainer() {
        return core_catalogcontainer;
    }

    public void setCore_catalogcontainer(core_CatalogContainer core_catalogcontainer) {
        this.core_catalogcontainer = core_catalogcontainer;
    }
    public List<core_CatalogContainer> getCore_catalogcontainers() {
        return core_catalogcontainers;
    }

    public void addCore_catalogcontainer(Core_catalogcontainer core_catalogcontainer) {
        this.core_catalogcontainers.add(core_catalogcontainer);
    }

}
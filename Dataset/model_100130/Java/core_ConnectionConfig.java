





import java.util.List;
import java.util.ArrayList;

public class core_ConnectionConfig  {

    private String vendor;
    private boolean persistent;
    private String url;
    private String version;
    private String catalog;





    private core_CatalogContainer core_catalogcontainer;


    public core_ConnectionConfig(
        String vendor,        boolean persistent,        String url,        String version,        String catalog    ) {
        this.vendor = vendor;
        this.persistent = persistent;
        this.url = url;
        this.version = version;
        this.catalog = catalog;
    }


    public String getVendor() {
        return vendor;
    }

    public void setVendor(String vendor) {
        this.vendor = vendor;
    }
    public boolean getPersistent() {
        return persistent;
    }

    public void setPersistent(boolean persistent) {
        this.persistent = persistent;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getCatalog() {
        return catalog;
    }

    public void setCatalog(String catalog) {
        this.catalog = catalog;
    }

    public core_CatalogContainer getCore_catalogcontainer() {
        return core_catalogcontainer;
    }

    public void setCore_catalogcontainer(core_CatalogContainer core_catalogcontainer) {
        this.core_catalogcontainer = core_catalogcontainer;
    }

}
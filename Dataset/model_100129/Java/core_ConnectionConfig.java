





import java.util.List;
import java.util.ArrayList;

public class core_ConnectionConfig extends ServiceConfig {

    private String url;
    private String catalog;
    private boolean persistent;
    private String version;
    private String vendor;



    public core_ConnectionConfig(
        String url,        String catalog,        boolean persistent,        String version,        String vendor    ) {
        super(
        );
        this.url = url;
        this.catalog = catalog;
        this.persistent = persistent;
        this.version = version;
        this.vendor = vendor;
    }


    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }
    public String getCatalog() {
        return catalog;
    }

    public void setCatalog(String catalog) {
        this.catalog = catalog;
    }
    public boolean getPersistent() {
        return persistent;
    }

    public void setPersistent(boolean persistent) {
        this.persistent = persistent;
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


}






import java.util.List;
import java.util.ArrayList;

public class sourcecleaner_Manifest extends Source {

    private String symbolicName;
    private String executionEnvironment;
    private boolean singleton;
    private String versionId;
    private String version;
    private boolean diagraph;
    private boolean lazy;
    private String versionQualifier;
    private String vendor;



    public sourcecleaner_Manifest(
        String symbolicName,        String executionEnvironment,        boolean singleton,        String versionId,        String version,        boolean diagraph,        boolean lazy,        String versionQualifier,        String vendor    ) {
        super(
        );
        this.symbolicName = symbolicName;
        this.executionEnvironment = executionEnvironment;
        this.singleton = singleton;
        this.versionId = versionId;
        this.version = version;
        this.diagraph = diagraph;
        this.lazy = lazy;
        this.versionQualifier = versionQualifier;
        this.vendor = vendor;
    }


    public String getSymbolicname() {
        return symbolicName;
    }

    public void setSymbolicname(String symbolicName) {
        this.symbolicName = symbolicName;
    }
    public String getExecutionenvironment() {
        return executionEnvironment;
    }

    public void setExecutionenvironment(String executionEnvironment) {
        this.executionEnvironment = executionEnvironment;
    }
    public boolean getSingleton() {
        return singleton;
    }

    public void setSingleton(boolean singleton) {
        this.singleton = singleton;
    }
    public String getVersionid() {
        return versionId;
    }

    public void setVersionid(String versionId) {
        this.versionId = versionId;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public boolean getDiagraph() {
        return diagraph;
    }

    public void setDiagraph(boolean diagraph) {
        this.diagraph = diagraph;
    }
    public boolean getLazy() {
        return lazy;
    }

    public void setLazy(boolean lazy) {
        this.lazy = lazy;
    }
    public String getVersionqualifier() {
        return versionQualifier;
    }

    public void setVersionqualifier(String versionQualifier) {
        this.versionQualifier = versionQualifier;
    }
    public String getVendor() {
        return vendor;
    }

    public void setVendor(String vendor) {
        this.vendor = vendor;
    }


}
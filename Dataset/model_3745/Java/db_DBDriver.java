





import java.util.List;
import java.util.ArrayList;

public class db_DBDriver extends DBResource {

    private String urlRegexPattern;
    private boolean pooling;
    private String websiteUrl;
    private String guideUrl;
    private String exampleUrl;
    private String driverClassName;
    private boolean default;
    private String jars;
    private int defaultPort;



    public db_DBDriver(
        String urlRegexPattern,        boolean pooling,        String websiteUrl,        String guideUrl,        String exampleUrl,        String driverClassName,        boolean default,        String jars,        int defaultPort    ) {
        super(
        );
        this.urlRegexPattern = urlRegexPattern;
        this.pooling = pooling;
        this.websiteUrl = websiteUrl;
        this.guideUrl = guideUrl;
        this.exampleUrl = exampleUrl;
        this.driverClassName = driverClassName;
        this.default = default;
        this.jars = jars;
        this.defaultPort = defaultPort;
    }


    public String getUrlregexpattern() {
        return urlRegexPattern;
    }

    public void setUrlregexpattern(String urlRegexPattern) {
        this.urlRegexPattern = urlRegexPattern;
    }
    public boolean getPooling() {
        return pooling;
    }

    public void setPooling(boolean pooling) {
        this.pooling = pooling;
    }
    public String getWebsiteurl() {
        return websiteUrl;
    }

    public void setWebsiteurl(String websiteUrl) {
        this.websiteUrl = websiteUrl;
    }
    public String getGuideurl() {
        return guideUrl;
    }

    public void setGuideurl(String guideUrl) {
        this.guideUrl = guideUrl;
    }
    public String getExampleurl() {
        return exampleUrl;
    }

    public void setExampleurl(String exampleUrl) {
        this.exampleUrl = exampleUrl;
    }
    public String getDriverclassname() {
        return driverClassName;
    }

    public void setDriverclassname(String driverClassName) {
        this.driverClassName = driverClassName;
    }
    public boolean getDefault() {
        return default;
    }

    public void setDefault(boolean default) {
        this.default = default;
    }
    public String getJars() {
        return jars;
    }

    public void setJars(String jars) {
        this.jars = jars;
    }
    public int getDefaultport() {
        return defaultPort;
    }

    public void setDefaultport(int defaultPort) {
        this.defaultPort = defaultPort;
    }


}
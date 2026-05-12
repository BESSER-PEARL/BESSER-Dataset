





import java.util.List;
import java.util.ArrayList;

public class db_DBDriver extends DBResource {

    private String driverClassName;
    private String jars;
    private int defaultPort;
    private boolean default;
    private String guideUrl;
    private String exampleUrl;
    private String websiteUrl;
    private boolean pooling;
    private String urlRegexPattern;



    public db_DBDriver(
        String driverClassName,        String jars,        int defaultPort,        boolean default,        String guideUrl,        String exampleUrl,        String websiteUrl,        boolean pooling,        String urlRegexPattern    ) {
        super(
        );
        this.driverClassName = driverClassName;
        this.jars = jars;
        this.defaultPort = defaultPort;
        this.default = default;
        this.guideUrl = guideUrl;
        this.exampleUrl = exampleUrl;
        this.websiteUrl = websiteUrl;
        this.pooling = pooling;
        this.urlRegexPattern = urlRegexPattern;
    }


    public String getDriverclassname() {
        return driverClassName;
    }

    public void setDriverclassname(String driverClassName) {
        this.driverClassName = driverClassName;
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
    public boolean getDefault() {
        return default;
    }

    public void setDefault(boolean default) {
        this.default = default;
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
    public String getWebsiteurl() {
        return websiteUrl;
    }

    public void setWebsiteurl(String websiteUrl) {
        this.websiteUrl = websiteUrl;
    }
    public boolean getPooling() {
        return pooling;
    }

    public void setPooling(boolean pooling) {
        this.pooling = pooling;
    }
    public String getUrlregexpattern() {
        return urlRegexPattern;
    }

    public void setUrlregexpattern(String urlRegexPattern) {
        this.urlRegexPattern = urlRegexPattern;
    }


}
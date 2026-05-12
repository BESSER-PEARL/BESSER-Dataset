





import java.util.List;
import java.util.ArrayList;

public class connection_SalesforceSchemaConnection extends Connection {

    private String batchSize;
    private String moduleName;
    private boolean useAlphbet;
    private String proxyPort;
    private boolean useProxy;
    private String proxyUsername;
    private boolean useCustomModuleName;
    private String webServiceUrl;
    private boolean useHttpProxy;
    private String timeOut;
    private String proxyHost;
    private String queryCondition;
    private String proxyPassword;
    private String userName;
    private String password;



    public connection_SalesforceSchemaConnection(
        String batchSize,        String moduleName,        boolean useAlphbet,        String proxyPort,        boolean useProxy,        String proxyUsername,        boolean useCustomModuleName,        String webServiceUrl,        boolean useHttpProxy,        String timeOut,        String proxyHost,        String queryCondition,        String proxyPassword,        String userName,        String password    ) {
        super(
        );
        this.batchSize = batchSize;
        this.moduleName = moduleName;
        this.useAlphbet = useAlphbet;
        this.proxyPort = proxyPort;
        this.useProxy = useProxy;
        this.proxyUsername = proxyUsername;
        this.useCustomModuleName = useCustomModuleName;
        this.webServiceUrl = webServiceUrl;
        this.useHttpProxy = useHttpProxy;
        this.timeOut = timeOut;
        this.proxyHost = proxyHost;
        this.queryCondition = queryCondition;
        this.proxyPassword = proxyPassword;
        this.userName = userName;
        this.password = password;
    }


    public String getBatchsize() {
        return batchSize;
    }

    public void setBatchsize(String batchSize) {
        this.batchSize = batchSize;
    }
    public String getModulename() {
        return moduleName;
    }

    public void setModulename(String moduleName) {
        this.moduleName = moduleName;
    }
    public boolean getUsealphbet() {
        return useAlphbet;
    }

    public void setUsealphbet(boolean useAlphbet) {
        this.useAlphbet = useAlphbet;
    }
    public String getProxyport() {
        return proxyPort;
    }

    public void setProxyport(String proxyPort) {
        this.proxyPort = proxyPort;
    }
    public boolean getUseproxy() {
        return useProxy;
    }

    public void setUseproxy(boolean useProxy) {
        this.useProxy = useProxy;
    }
    public String getProxyusername() {
        return proxyUsername;
    }

    public void setProxyusername(String proxyUsername) {
        this.proxyUsername = proxyUsername;
    }
    public boolean getUsecustommodulename() {
        return useCustomModuleName;
    }

    public void setUsecustommodulename(boolean useCustomModuleName) {
        this.useCustomModuleName = useCustomModuleName;
    }
    public String getWebserviceurl() {
        return webServiceUrl;
    }

    public void setWebserviceurl(String webServiceUrl) {
        this.webServiceUrl = webServiceUrl;
    }
    public boolean getUsehttpproxy() {
        return useHttpProxy;
    }

    public void setUsehttpproxy(boolean useHttpProxy) {
        this.useHttpProxy = useHttpProxy;
    }
    public String getTimeout() {
        return timeOut;
    }

    public void setTimeout(String timeOut) {
        this.timeOut = timeOut;
    }
    public String getProxyhost() {
        return proxyHost;
    }

    public void setProxyhost(String proxyHost) {
        this.proxyHost = proxyHost;
    }
    public String getQuerycondition() {
        return queryCondition;
    }

    public void setQuerycondition(String queryCondition) {
        this.queryCondition = queryCondition;
    }
    public String getProxypassword() {
        return proxyPassword;
    }

    public void setProxypassword(String proxyPassword) {
        this.proxyPassword = proxyPassword;
    }
    public String getUsername() {
        return userName;
    }

    public void setUsername(String userName) {
        this.userName = userName;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }


}
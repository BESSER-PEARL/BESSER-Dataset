





import java.util.List;
import java.util.ArrayList;

public class connection_SalesforceSchemaConnection extends Connection {

    private String moduleName;
    private String batchSize;
    private String proxyUsername;
    private boolean useCustomModuleName;
    private String userName;
    private String webServiceUrl;
    private boolean useProxy;
    private boolean useHttpProxy;
    private String proxyPassword;
    private boolean useAlphbet;
    private String proxyHost;
    private String proxyPort;
    private String timeOut;
    private String queryCondition;
    private String password;



    public connection_SalesforceSchemaConnection(
        String moduleName,        String batchSize,        String proxyUsername,        boolean useCustomModuleName,        String userName,        String webServiceUrl,        boolean useProxy,        boolean useHttpProxy,        String proxyPassword,        boolean useAlphbet,        String proxyHost,        String proxyPort,        String timeOut,        String queryCondition,        String password    ) {
        super(
        );
        this.moduleName = moduleName;
        this.batchSize = batchSize;
        this.proxyUsername = proxyUsername;
        this.useCustomModuleName = useCustomModuleName;
        this.userName = userName;
        this.webServiceUrl = webServiceUrl;
        this.useProxy = useProxy;
        this.useHttpProxy = useHttpProxy;
        this.proxyPassword = proxyPassword;
        this.useAlphbet = useAlphbet;
        this.proxyHost = proxyHost;
        this.proxyPort = proxyPort;
        this.timeOut = timeOut;
        this.queryCondition = queryCondition;
        this.password = password;
    }


    public String getModulename() {
        return moduleName;
    }

    public void setModulename(String moduleName) {
        this.moduleName = moduleName;
    }
    public String getBatchsize() {
        return batchSize;
    }

    public void setBatchsize(String batchSize) {
        this.batchSize = batchSize;
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
    public String getUsername() {
        return userName;
    }

    public void setUsername(String userName) {
        this.userName = userName;
    }
    public String getWebserviceurl() {
        return webServiceUrl;
    }

    public void setWebserviceurl(String webServiceUrl) {
        this.webServiceUrl = webServiceUrl;
    }
    public boolean getUseproxy() {
        return useProxy;
    }

    public void setUseproxy(boolean useProxy) {
        this.useProxy = useProxy;
    }
    public boolean getUsehttpproxy() {
        return useHttpProxy;
    }

    public void setUsehttpproxy(boolean useHttpProxy) {
        this.useHttpProxy = useHttpProxy;
    }
    public String getProxypassword() {
        return proxyPassword;
    }

    public void setProxypassword(String proxyPassword) {
        this.proxyPassword = proxyPassword;
    }
    public boolean getUsealphbet() {
        return useAlphbet;
    }

    public void setUsealphbet(boolean useAlphbet) {
        this.useAlphbet = useAlphbet;
    }
    public String getProxyhost() {
        return proxyHost;
    }

    public void setProxyhost(String proxyHost) {
        this.proxyHost = proxyHost;
    }
    public String getProxyport() {
        return proxyPort;
    }

    public void setProxyport(String proxyPort) {
        this.proxyPort = proxyPort;
    }
    public String getTimeout() {
        return timeOut;
    }

    public void setTimeout(String timeOut) {
        this.timeOut = timeOut;
    }
    public String getQuerycondition() {
        return queryCondition;
    }

    public void setQuerycondition(String queryCondition) {
        this.queryCondition = queryCondition;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }


}
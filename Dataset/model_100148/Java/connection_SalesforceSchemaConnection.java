





import java.util.List;
import java.util.ArrayList;

public class connection_SalesforceSchemaConnection extends Connection {

    private boolean useProxy;
    private String userName;
    private String webServiceUrl;
    private String proxyPort;
    private String timeOut;
    private String batchSize;
    private String password;
    private boolean useAlphbet;
    private boolean useHttpProxy;
    private String proxyUsername;
    private String proxyHost;
    private String moduleName;
    private String queryCondition;
    private boolean useCustomModuleName;
    private String proxyPassword;



    public connection_SalesforceSchemaConnection(
        boolean useProxy,        String userName,        String webServiceUrl,        String proxyPort,        String timeOut,        String batchSize,        String password,        boolean useAlphbet,        boolean useHttpProxy,        String proxyUsername,        String proxyHost,        String moduleName,        String queryCondition,        boolean useCustomModuleName,        String proxyPassword    ) {
        super(
        );
        this.useProxy = useProxy;
        this.userName = userName;
        this.webServiceUrl = webServiceUrl;
        this.proxyPort = proxyPort;
        this.timeOut = timeOut;
        this.batchSize = batchSize;
        this.password = password;
        this.useAlphbet = useAlphbet;
        this.useHttpProxy = useHttpProxy;
        this.proxyUsername = proxyUsername;
        this.proxyHost = proxyHost;
        this.moduleName = moduleName;
        this.queryCondition = queryCondition;
        this.useCustomModuleName = useCustomModuleName;
        this.proxyPassword = proxyPassword;
    }


    public boolean getUseproxy() {
        return useProxy;
    }

    public void setUseproxy(boolean useProxy) {
        this.useProxy = useProxy;
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
    public String getBatchsize() {
        return batchSize;
    }

    public void setBatchsize(String batchSize) {
        this.batchSize = batchSize;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public boolean getUsealphbet() {
        return useAlphbet;
    }

    public void setUsealphbet(boolean useAlphbet) {
        this.useAlphbet = useAlphbet;
    }
    public boolean getUsehttpproxy() {
        return useHttpProxy;
    }

    public void setUsehttpproxy(boolean useHttpProxy) {
        this.useHttpProxy = useHttpProxy;
    }
    public String getProxyusername() {
        return proxyUsername;
    }

    public void setProxyusername(String proxyUsername) {
        this.proxyUsername = proxyUsername;
    }
    public String getProxyhost() {
        return proxyHost;
    }

    public void setProxyhost(String proxyHost) {
        this.proxyHost = proxyHost;
    }
    public String getModulename() {
        return moduleName;
    }

    public void setModulename(String moduleName) {
        this.moduleName = moduleName;
    }
    public String getQuerycondition() {
        return queryCondition;
    }

    public void setQuerycondition(String queryCondition) {
        this.queryCondition = queryCondition;
    }
    public boolean getUsecustommodulename() {
        return useCustomModuleName;
    }

    public void setUsecustommodulename(boolean useCustomModuleName) {
        this.useCustomModuleName = useCustomModuleName;
    }
    public String getProxypassword() {
        return proxyPassword;
    }

    public void setProxypassword(String proxyPassword) {
        this.proxyPassword = proxyPassword;
    }


}
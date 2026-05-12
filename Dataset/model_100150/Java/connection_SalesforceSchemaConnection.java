





import java.util.List;
import java.util.ArrayList;

public class connection_SalesforceSchemaConnection extends Connection {

    private String timeOut;
    private boolean useProxy;
    private String moduleName;
    private String queryCondition;
    private boolean useHttpProxy;
    private String proxyHost;
    private String proxyPort;
    private String batchSize;
    private String proxyUsername;
    private String password;
    private boolean useCustomModuleName;
    private String webServiceUrl;
    private boolean useAlphbet;
    private String userName;
    private String proxyPassword;



    public connection_SalesforceSchemaConnection(
        String timeOut,        boolean useProxy,        String moduleName,        String queryCondition,        boolean useHttpProxy,        String proxyHost,        String proxyPort,        String batchSize,        String proxyUsername,        String password,        boolean useCustomModuleName,        String webServiceUrl,        boolean useAlphbet,        String userName,        String proxyPassword    ) {
        super(
        );
        this.timeOut = timeOut;
        this.useProxy = useProxy;
        this.moduleName = moduleName;
        this.queryCondition = queryCondition;
        this.useHttpProxy = useHttpProxy;
        this.proxyHost = proxyHost;
        this.proxyPort = proxyPort;
        this.batchSize = batchSize;
        this.proxyUsername = proxyUsername;
        this.password = password;
        this.useCustomModuleName = useCustomModuleName;
        this.webServiceUrl = webServiceUrl;
        this.useAlphbet = useAlphbet;
        this.userName = userName;
        this.proxyPassword = proxyPassword;
    }


    public String getTimeout() {
        return timeOut;
    }

    public void setTimeout(String timeOut) {
        this.timeOut = timeOut;
    }
    public boolean getUseproxy() {
        return useProxy;
    }

    public void setUseproxy(boolean useProxy) {
        this.useProxy = useProxy;
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
    public boolean getUsehttpproxy() {
        return useHttpProxy;
    }

    public void setUsehttpproxy(boolean useHttpProxy) {
        this.useHttpProxy = useHttpProxy;
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
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
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
    public boolean getUsealphbet() {
        return useAlphbet;
    }

    public void setUsealphbet(boolean useAlphbet) {
        this.useAlphbet = useAlphbet;
    }
    public String getUsername() {
        return userName;
    }

    public void setUsername(String userName) {
        this.userName = userName;
    }
    public String getProxypassword() {
        return proxyPassword;
    }

    public void setProxypassword(String proxyPassword) {
        this.proxyPassword = proxyPassword;
    }


}
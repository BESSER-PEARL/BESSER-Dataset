





import java.util.List;
import java.util.ArrayList;

public class connection_SalesforceSchemaConnection extends Connection {

    private boolean useHttpProxy;
    private String proxyPassword;
    private boolean useProxy;
    private boolean useCustomModuleName;
    private String queryCondition;
    private String timeOut;
    private String userName;
    private String webServiceUrl;
    private String batchSize;
    private String proxyUsername;
    private String password;
    private boolean useAlphbet;
    private String proxyPort;
    private String moduleName;
    private String proxyHost;



    public connection_SalesforceSchemaConnection(
        boolean useHttpProxy,        String proxyPassword,        boolean useProxy,        boolean useCustomModuleName,        String queryCondition,        String timeOut,        String userName,        String webServiceUrl,        String batchSize,        String proxyUsername,        String password,        boolean useAlphbet,        String proxyPort,        String moduleName,        String proxyHost    ) {
        super(
        );
        this.useHttpProxy = useHttpProxy;
        this.proxyPassword = proxyPassword;
        this.useProxy = useProxy;
        this.useCustomModuleName = useCustomModuleName;
        this.queryCondition = queryCondition;
        this.timeOut = timeOut;
        this.userName = userName;
        this.webServiceUrl = webServiceUrl;
        this.batchSize = batchSize;
        this.proxyUsername = proxyUsername;
        this.password = password;
        this.useAlphbet = useAlphbet;
        this.proxyPort = proxyPort;
        this.moduleName = moduleName;
        this.proxyHost = proxyHost;
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
    public boolean getUseproxy() {
        return useProxy;
    }

    public void setUseproxy(boolean useProxy) {
        this.useProxy = useProxy;
    }
    public boolean getUsecustommodulename() {
        return useCustomModuleName;
    }

    public void setUsecustommodulename(boolean useCustomModuleName) {
        this.useCustomModuleName = useCustomModuleName;
    }
    public String getQuerycondition() {
        return queryCondition;
    }

    public void setQuerycondition(String queryCondition) {
        this.queryCondition = queryCondition;
    }
    public String getTimeout() {
        return timeOut;
    }

    public void setTimeout(String timeOut) {
        this.timeOut = timeOut;
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
    public String getModulename() {
        return moduleName;
    }

    public void setModulename(String moduleName) {
        this.moduleName = moduleName;
    }
    public String getProxyhost() {
        return proxyHost;
    }

    public void setProxyhost(String proxyHost) {
        this.proxyHost = proxyHost;
    }


}






import java.util.List;
import java.util.ArrayList;

public class connection_SalesforceSchemaConnection extends Connection {

    private String password;
    private String timeOut;
    private String proxyPort;
    private boolean useAlphbet;
    private boolean useCustomModuleName;
    private boolean useProxy;
    private String batchSize;
    private String webServiceUrl;
    private String moduleName;
    private String userName;
    private String proxyUsername;
    private String proxyHost;
    private String proxyPassword;
    private boolean useHttpProxy;
    private String queryCondition;



    public connection_SalesforceSchemaConnection(
        String password,        String timeOut,        String proxyPort,        boolean useAlphbet,        boolean useCustomModuleName,        boolean useProxy,        String batchSize,        String webServiceUrl,        String moduleName,        String userName,        String proxyUsername,        String proxyHost,        String proxyPassword,        boolean useHttpProxy,        String queryCondition    ) {
        super(
        );
        this.password = password;
        this.timeOut = timeOut;
        this.proxyPort = proxyPort;
        this.useAlphbet = useAlphbet;
        this.useCustomModuleName = useCustomModuleName;
        this.useProxy = useProxy;
        this.batchSize = batchSize;
        this.webServiceUrl = webServiceUrl;
        this.moduleName = moduleName;
        this.userName = userName;
        this.proxyUsername = proxyUsername;
        this.proxyHost = proxyHost;
        this.proxyPassword = proxyPassword;
        this.useHttpProxy = useHttpProxy;
        this.queryCondition = queryCondition;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getTimeout() {
        return timeOut;
    }

    public void setTimeout(String timeOut) {
        this.timeOut = timeOut;
    }
    public String getProxyport() {
        return proxyPort;
    }

    public void setProxyport(String proxyPort) {
        this.proxyPort = proxyPort;
    }
    public boolean getUsealphbet() {
        return useAlphbet;
    }

    public void setUsealphbet(boolean useAlphbet) {
        this.useAlphbet = useAlphbet;
    }
    public boolean getUsecustommodulename() {
        return useCustomModuleName;
    }

    public void setUsecustommodulename(boolean useCustomModuleName) {
        this.useCustomModuleName = useCustomModuleName;
    }
    public boolean getUseproxy() {
        return useProxy;
    }

    public void setUseproxy(boolean useProxy) {
        this.useProxy = useProxy;
    }
    public String getBatchsize() {
        return batchSize;
    }

    public void setBatchsize(String batchSize) {
        this.batchSize = batchSize;
    }
    public String getWebserviceurl() {
        return webServiceUrl;
    }

    public void setWebserviceurl(String webServiceUrl) {
        this.webServiceUrl = webServiceUrl;
    }
    public String getModulename() {
        return moduleName;
    }

    public void setModulename(String moduleName) {
        this.moduleName = moduleName;
    }
    public String getUsername() {
        return userName;
    }

    public void setUsername(String userName) {
        this.userName = userName;
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
    public String getProxypassword() {
        return proxyPassword;
    }

    public void setProxypassword(String proxyPassword) {
        this.proxyPassword = proxyPassword;
    }
    public boolean getUsehttpproxy() {
        return useHttpProxy;
    }

    public void setUsehttpproxy(boolean useHttpProxy) {
        this.useHttpProxy = useHttpProxy;
    }
    public String getQuerycondition() {
        return queryCondition;
    }

    public void setQuerycondition(String queryCondition) {
        this.queryCondition = queryCondition;
    }


}
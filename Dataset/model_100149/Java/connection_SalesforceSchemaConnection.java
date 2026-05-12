





import java.util.List;
import java.util.ArrayList;

public class connection_SalesforceSchemaConnection extends Connection {

    private String queryCondition;
    private boolean useHttpProxy;
    private String callbackHost;
    private String batchSize;
    private String loginType;
    private String salesforceVersion;
    private String proxyPort;
    private String proxyHost;
    private String callbackPort;
    private String token;
    private String moduleName;
    private String webServiceUrlTextForOAuth;
    private String timeOut;
    private boolean useCustomModuleName;
    private String password;
    private boolean useAlphbet;
    private String consumeKey;
    private boolean useProxy;
    private String proxyPassword;
    private String consumeSecret;
    private String proxyUsername;
    private String webServiceUrl;
    private String userName;





    private connection_SalesforceModuleUnit connection_salesforcemoduleunit;




    private List<connection_SalesforceModuleUnit> connection_salesforcemoduleunits;


    public connection_SalesforceSchemaConnection(
        String queryCondition,        boolean useHttpProxy,        String callbackHost,        String batchSize,        String loginType,        String salesforceVersion,        String proxyPort,        String proxyHost,        String callbackPort,        String token,        String moduleName,        String webServiceUrlTextForOAuth,        String timeOut,        boolean useCustomModuleName,        String password,        boolean useAlphbet,        String consumeKey,        boolean useProxy,        String proxyPassword,        String consumeSecret,        String proxyUsername,        String webServiceUrl,        String userName    ) {
        super(
        );
        this.queryCondition = queryCondition;
        this.useHttpProxy = useHttpProxy;
        this.callbackHost = callbackHost;
        this.batchSize = batchSize;
        this.loginType = loginType;
        this.salesforceVersion = salesforceVersion;
        this.proxyPort = proxyPort;
        this.proxyHost = proxyHost;
        this.callbackPort = callbackPort;
        this.token = token;
        this.moduleName = moduleName;
        this.webServiceUrlTextForOAuth = webServiceUrlTextForOAuth;
        this.timeOut = timeOut;
        this.useCustomModuleName = useCustomModuleName;
        this.password = password;
        this.useAlphbet = useAlphbet;
        this.consumeKey = consumeKey;
        this.useProxy = useProxy;
        this.proxyPassword = proxyPassword;
        this.consumeSecret = consumeSecret;
        this.proxyUsername = proxyUsername;
        this.webServiceUrl = webServiceUrl;
        this.userName = userName;
        this.connection_salesforcemoduleunits = new ArrayList<>();
    }

    public connection_SalesforceSchemaConnection(
        String queryCondition,        boolean useHttpProxy,        String callbackHost,        String batchSize,        String loginType,        String salesforceVersion,        String proxyPort,        String proxyHost,        String callbackPort,        String token,        String moduleName,        String webServiceUrlTextForOAuth,        String timeOut,        boolean useCustomModuleName,        String password,        boolean useAlphbet,        String consumeKey,        boolean useProxy,        String proxyPassword,        String consumeSecret,        String proxyUsername,        String webServiceUrl,        String userName        ArrayList<connection_SalesforceModuleUnit> connection_salesforcemoduleunits    ) {
        this.queryCondition = queryCondition;
        this.useHttpProxy = useHttpProxy;
        this.callbackHost = callbackHost;
        this.batchSize = batchSize;
        this.loginType = loginType;
        this.salesforceVersion = salesforceVersion;
        this.proxyPort = proxyPort;
        this.proxyHost = proxyHost;
        this.callbackPort = callbackPort;
        this.token = token;
        this.moduleName = moduleName;
        this.webServiceUrlTextForOAuth = webServiceUrlTextForOAuth;
        this.timeOut = timeOut;
        this.useCustomModuleName = useCustomModuleName;
        this.password = password;
        this.useAlphbet = useAlphbet;
        this.consumeKey = consumeKey;
        this.useProxy = useProxy;
        this.proxyPassword = proxyPassword;
        this.consumeSecret = consumeSecret;
        this.proxyUsername = proxyUsername;
        this.webServiceUrl = webServiceUrl;
        this.userName = userName;
        this.connection_salesforcemoduleunits = connection_salesforcemoduleunits;
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
    public String getCallbackhost() {
        return callbackHost;
    }

    public void setCallbackhost(String callbackHost) {
        this.callbackHost = callbackHost;
    }
    public String getBatchsize() {
        return batchSize;
    }

    public void setBatchsize(String batchSize) {
        this.batchSize = batchSize;
    }
    public String getLogintype() {
        return loginType;
    }

    public void setLogintype(String loginType) {
        this.loginType = loginType;
    }
    public String getSalesforceversion() {
        return salesforceVersion;
    }

    public void setSalesforceversion(String salesforceVersion) {
        this.salesforceVersion = salesforceVersion;
    }
    public String getProxyport() {
        return proxyPort;
    }

    public void setProxyport(String proxyPort) {
        this.proxyPort = proxyPort;
    }
    public String getProxyhost() {
        return proxyHost;
    }

    public void setProxyhost(String proxyHost) {
        this.proxyHost = proxyHost;
    }
    public String getCallbackport() {
        return callbackPort;
    }

    public void setCallbackport(String callbackPort) {
        this.callbackPort = callbackPort;
    }
    public String getToken() {
        return token;
    }

    public void setToken(String token) {
        this.token = token;
    }
    public String getModulename() {
        return moduleName;
    }

    public void setModulename(String moduleName) {
        this.moduleName = moduleName;
    }
    public String getWebserviceurltextforoauth() {
        return webServiceUrlTextForOAuth;
    }

    public void setWebserviceurltextforoauth(String webServiceUrlTextForOAuth) {
        this.webServiceUrlTextForOAuth = webServiceUrlTextForOAuth;
    }
    public String getTimeout() {
        return timeOut;
    }

    public void setTimeout(String timeOut) {
        this.timeOut = timeOut;
    }
    public boolean getUsecustommodulename() {
        return useCustomModuleName;
    }

    public void setUsecustommodulename(boolean useCustomModuleName) {
        this.useCustomModuleName = useCustomModuleName;
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
    public String getConsumekey() {
        return consumeKey;
    }

    public void setConsumekey(String consumeKey) {
        this.consumeKey = consumeKey;
    }
    public boolean getUseproxy() {
        return useProxy;
    }

    public void setUseproxy(boolean useProxy) {
        this.useProxy = useProxy;
    }
    public String getProxypassword() {
        return proxyPassword;
    }

    public void setProxypassword(String proxyPassword) {
        this.proxyPassword = proxyPassword;
    }
    public String getConsumesecret() {
        return consumeSecret;
    }

    public void setConsumesecret(String consumeSecret) {
        this.consumeSecret = consumeSecret;
    }
    public String getProxyusername() {
        return proxyUsername;
    }

    public void setProxyusername(String proxyUsername) {
        this.proxyUsername = proxyUsername;
    }
    public String getWebserviceurl() {
        return webServiceUrl;
    }

    public void setWebserviceurl(String webServiceUrl) {
        this.webServiceUrl = webServiceUrl;
    }
    public String getUsername() {
        return userName;
    }

    public void setUsername(String userName) {
        this.userName = userName;
    }

    public connection_SalesforceModuleUnit getConnection_salesforcemoduleunit() {
        return connection_salesforcemoduleunit;
    }

    public void setConnection_salesforcemoduleunit(connection_SalesforceModuleUnit connection_salesforcemoduleunit) {
        this.connection_salesforcemoduleunit = connection_salesforcemoduleunit;
    }
    public List<connection_SalesforceModuleUnit> getConnection_salesforcemoduleunits() {
        return connection_salesforcemoduleunits;
    }

    public void addConnection_salesforcemoduleunit(Connection_salesforcemoduleunit connection_salesforcemoduleunit) {
        this.connection_salesforcemoduleunits.add(connection_salesforcemoduleunit);
    }

}






import java.util.List;
import java.util.ArrayList;

public class connection_WSDLSchemaConnection extends Connection {

    private boolean useProxy;
    private String proxyHost;
    private String Encoding;
    private String EndpointURI;
    private String Password;
    private String proxyPort;
    private String parameters;
    private boolean needAuth;
    private String methodName;
    private String Value;
    private String WSDL;
    private int timeOut;
    private String proxyUser;
    private String proxyPassword;
    private String UserName;



    public connection_WSDLSchemaConnection(
        boolean useProxy,        String proxyHost,        String Encoding,        String EndpointURI,        String Password,        String proxyPort,        String parameters,        boolean needAuth,        String methodName,        String Value,        String WSDL,        int timeOut,        String proxyUser,        String proxyPassword,        String UserName    ) {
        super(
        );
        this.useProxy = useProxy;
        this.proxyHost = proxyHost;
        this.Encoding = Encoding;
        this.EndpointURI = EndpointURI;
        this.Password = Password;
        this.proxyPort = proxyPort;
        this.parameters = parameters;
        this.needAuth = needAuth;
        this.methodName = methodName;
        this.Value = Value;
        this.WSDL = WSDL;
        this.timeOut = timeOut;
        this.proxyUser = proxyUser;
        this.proxyPassword = proxyPassword;
        this.UserName = UserName;
    }


    public boolean getUseproxy() {
        return useProxy;
    }

    public void setUseproxy(boolean useProxy) {
        this.useProxy = useProxy;
    }
    public String getProxyhost() {
        return proxyHost;
    }

    public void setProxyhost(String proxyHost) {
        this.proxyHost = proxyHost;
    }
    public String getEncoding() {
        return Encoding;
    }

    public void setEncoding(String Encoding) {
        this.Encoding = Encoding;
    }
    public String getEndpointuri() {
        return EndpointURI;
    }

    public void setEndpointuri(String EndpointURI) {
        this.EndpointURI = EndpointURI;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getProxyport() {
        return proxyPort;
    }

    public void setProxyport(String proxyPort) {
        this.proxyPort = proxyPort;
    }
    public String getParameters() {
        return parameters;
    }

    public void setParameters(String parameters) {
        this.parameters = parameters;
    }
    public boolean getNeedauth() {
        return needAuth;
    }

    public void setNeedauth(boolean needAuth) {
        this.needAuth = needAuth;
    }
    public String getMethodname() {
        return methodName;
    }

    public void setMethodname(String methodName) {
        this.methodName = methodName;
    }
    public String getValue() {
        return Value;
    }

    public void setValue(String Value) {
        this.Value = Value;
    }
    public String getWsdl() {
        return WSDL;
    }

    public void setWsdl(String WSDL) {
        this.WSDL = WSDL;
    }
    public int getTimeout() {
        return timeOut;
    }

    public void setTimeout(int timeOut) {
        this.timeOut = timeOut;
    }
    public String getProxyuser() {
        return proxyUser;
    }

    public void setProxyuser(String proxyUser) {
        this.proxyUser = proxyUser;
    }
    public String getProxypassword() {
        return proxyPassword;
    }

    public void setProxypassword(String proxyPassword) {
        this.proxyPassword = proxyPassword;
    }
    public String getUsername() {
        return UserName;
    }

    public void setUsername(String UserName) {
        this.UserName = UserName;
    }


}






import java.util.List;
import java.util.ArrayList;

public class connection_WSDLSchemaConnection extends Connection {

    private String methodName;
    private String proxyUser;
    private boolean needAuth;
    private boolean useProxy;
    private int timeOut;
    private String Password;
    private String EndpointURI;
    private String Value;
    private String Encoding;
    private String WSDL;
    private String proxyPassword;
    private String UserName;
    private String proxyHost;
    private String parameters;
    private String proxyPort;



    public connection_WSDLSchemaConnection(
        String methodName,        String proxyUser,        boolean needAuth,        boolean useProxy,        int timeOut,        String Password,        String EndpointURI,        String Value,        String Encoding,        String WSDL,        String proxyPassword,        String UserName,        String proxyHost,        String parameters,        String proxyPort    ) {
        super(
        );
        this.methodName = methodName;
        this.proxyUser = proxyUser;
        this.needAuth = needAuth;
        this.useProxy = useProxy;
        this.timeOut = timeOut;
        this.Password = Password;
        this.EndpointURI = EndpointURI;
        this.Value = Value;
        this.Encoding = Encoding;
        this.WSDL = WSDL;
        this.proxyPassword = proxyPassword;
        this.UserName = UserName;
        this.proxyHost = proxyHost;
        this.parameters = parameters;
        this.proxyPort = proxyPort;
    }


    public String getMethodname() {
        return methodName;
    }

    public void setMethodname(String methodName) {
        this.methodName = methodName;
    }
    public String getProxyuser() {
        return proxyUser;
    }

    public void setProxyuser(String proxyUser) {
        this.proxyUser = proxyUser;
    }
    public boolean getNeedauth() {
        return needAuth;
    }

    public void setNeedauth(boolean needAuth) {
        this.needAuth = needAuth;
    }
    public boolean getUseproxy() {
        return useProxy;
    }

    public void setUseproxy(boolean useProxy) {
        this.useProxy = useProxy;
    }
    public int getTimeout() {
        return timeOut;
    }

    public void setTimeout(int timeOut) {
        this.timeOut = timeOut;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getEndpointuri() {
        return EndpointURI;
    }

    public void setEndpointuri(String EndpointURI) {
        this.EndpointURI = EndpointURI;
    }
    public String getValue() {
        return Value;
    }

    public void setValue(String Value) {
        this.Value = Value;
    }
    public String getEncoding() {
        return Encoding;
    }

    public void setEncoding(String Encoding) {
        this.Encoding = Encoding;
    }
    public String getWsdl() {
        return WSDL;
    }

    public void setWsdl(String WSDL) {
        this.WSDL = WSDL;
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
    public String getProxyhost() {
        return proxyHost;
    }

    public void setProxyhost(String proxyHost) {
        this.proxyHost = proxyHost;
    }
    public String getParameters() {
        return parameters;
    }

    public void setParameters(String parameters) {
        this.parameters = parameters;
    }
    public String getProxyport() {
        return proxyPort;
    }

    public void setProxyport(String proxyPort) {
        this.proxyPort = proxyPort;
    }


}
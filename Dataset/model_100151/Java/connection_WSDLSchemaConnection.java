





import java.util.List;
import java.util.ArrayList;

public class connection_WSDLSchemaConnection extends Connection {

    private String proxyHost;
    private String WSDL;
    private String methodName;
    private String Password;
    private boolean needAuth;
    private int timeOut;
    private String proxyUser;
    private String proxyPassword;
    private String UserName;
    private String Encoding;
    private String proxyPort;
    private boolean useProxy;
    private String Value;
    private String parameters;
    private String EndpointURI;



    public connection_WSDLSchemaConnection(
        String proxyHost,        String WSDL,        String methodName,        String Password,        boolean needAuth,        int timeOut,        String proxyUser,        String proxyPassword,        String UserName,        String Encoding,        String proxyPort,        boolean useProxy,        String Value,        String parameters,        String EndpointURI    ) {
        super(
        );
        this.proxyHost = proxyHost;
        this.WSDL = WSDL;
        this.methodName = methodName;
        this.Password = Password;
        this.needAuth = needAuth;
        this.timeOut = timeOut;
        this.proxyUser = proxyUser;
        this.proxyPassword = proxyPassword;
        this.UserName = UserName;
        this.Encoding = Encoding;
        this.proxyPort = proxyPort;
        this.useProxy = useProxy;
        this.Value = Value;
        this.parameters = parameters;
        this.EndpointURI = EndpointURI;
    }


    public String getProxyhost() {
        return proxyHost;
    }

    public void setProxyhost(String proxyHost) {
        this.proxyHost = proxyHost;
    }
    public String getWsdl() {
        return WSDL;
    }

    public void setWsdl(String WSDL) {
        this.WSDL = WSDL;
    }
    public String getMethodname() {
        return methodName;
    }

    public void setMethodname(String methodName) {
        this.methodName = methodName;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public boolean getNeedauth() {
        return needAuth;
    }

    public void setNeedauth(boolean needAuth) {
        this.needAuth = needAuth;
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
    public String getEncoding() {
        return Encoding;
    }

    public void setEncoding(String Encoding) {
        this.Encoding = Encoding;
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
    public String getValue() {
        return Value;
    }

    public void setValue(String Value) {
        this.Value = Value;
    }
    public String getParameters() {
        return parameters;
    }

    public void setParameters(String parameters) {
        this.parameters = parameters;
    }
    public String getEndpointuri() {
        return EndpointURI;
    }

    public void setEndpointuri(String EndpointURI) {
        this.EndpointURI = EndpointURI;
    }


}
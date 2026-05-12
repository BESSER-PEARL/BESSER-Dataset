





import java.util.List;
import java.util.ArrayList;

public class connection_WSDLSchemaConnection extends Connection {

    private String parameters;
    private boolean isInputModel;
    private boolean needAuth;
    private String proxyHost;
    private String proxyPassword;
    private String Value;
    private String EndpointURI;
    private String serverName;
    private String WSDL;
    private String Encoding;
    private String proxyUser;
    private int timeOut;
    private String portNameSpace;
    private String UserName;
    private boolean useProxy;
    private String proxyPort;
    private String methodName;
    private String Password;
    private String serverNameSpace;
    private String portName;



    public connection_WSDLSchemaConnection(
        String parameters,        boolean isInputModel,        boolean needAuth,        String proxyHost,        String proxyPassword,        String Value,        String EndpointURI,        String serverName,        String WSDL,        String Encoding,        String proxyUser,        int timeOut,        String portNameSpace,        String UserName,        boolean useProxy,        String proxyPort,        String methodName,        String Password,        String serverNameSpace,        String portName    ) {
        super(
        );
        this.parameters = parameters;
        this.isInputModel = isInputModel;
        this.needAuth = needAuth;
        this.proxyHost = proxyHost;
        this.proxyPassword = proxyPassword;
        this.Value = Value;
        this.EndpointURI = EndpointURI;
        this.serverName = serverName;
        this.WSDL = WSDL;
        this.Encoding = Encoding;
        this.proxyUser = proxyUser;
        this.timeOut = timeOut;
        this.portNameSpace = portNameSpace;
        this.UserName = UserName;
        this.useProxy = useProxy;
        this.proxyPort = proxyPort;
        this.methodName = methodName;
        this.Password = Password;
        this.serverNameSpace = serverNameSpace;
        this.portName = portName;
    }


    public String getParameters() {
        return parameters;
    }

    public void setParameters(String parameters) {
        this.parameters = parameters;
    }
    public boolean getIsinputmodel() {
        return isInputModel;
    }

    public void setIsinputmodel(boolean isInputModel) {
        this.isInputModel = isInputModel;
    }
    public boolean getNeedauth() {
        return needAuth;
    }

    public void setNeedauth(boolean needAuth) {
        this.needAuth = needAuth;
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
    public String getValue() {
        return Value;
    }

    public void setValue(String Value) {
        this.Value = Value;
    }
    public String getEndpointuri() {
        return EndpointURI;
    }

    public void setEndpointuri(String EndpointURI) {
        this.EndpointURI = EndpointURI;
    }
    public String getServername() {
        return serverName;
    }

    public void setServername(String serverName) {
        this.serverName = serverName;
    }
    public String getWsdl() {
        return WSDL;
    }

    public void setWsdl(String WSDL) {
        this.WSDL = WSDL;
    }
    public String getEncoding() {
        return Encoding;
    }

    public void setEncoding(String Encoding) {
        this.Encoding = Encoding;
    }
    public String getProxyuser() {
        return proxyUser;
    }

    public void setProxyuser(String proxyUser) {
        this.proxyUser = proxyUser;
    }
    public int getTimeout() {
        return timeOut;
    }

    public void setTimeout(int timeOut) {
        this.timeOut = timeOut;
    }
    public String getPortnamespace() {
        return portNameSpace;
    }

    public void setPortnamespace(String portNameSpace) {
        this.portNameSpace = portNameSpace;
    }
    public String getUsername() {
        return UserName;
    }

    public void setUsername(String UserName) {
        this.UserName = UserName;
    }
    public boolean getUseproxy() {
        return useProxy;
    }

    public void setUseproxy(boolean useProxy) {
        this.useProxy = useProxy;
    }
    public String getProxyport() {
        return proxyPort;
    }

    public void setProxyport(String proxyPort) {
        this.proxyPort = proxyPort;
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
    public String getServernamespace() {
        return serverNameSpace;
    }

    public void setServernamespace(String serverNameSpace) {
        this.serverNameSpace = serverNameSpace;
    }
    public String getPortname() {
        return portName;
    }

    public void setPortname(String portName) {
        this.portName = portName;
    }


}






import java.util.List;
import java.util.ArrayList;

public class connection_WSDLSchemaConnection extends Connection {

    private String Password;
    private String proxyPassword;
    private String portName;
    private String Encoding;
    private String proxyUser;
    private boolean needAuth;
    private String serverName;
    private String parameters;
    private int timeOut;
    private String EndpointURI;
    private String portNameSpace;
    private boolean isInputModel;
    private String WSDL;
    private String proxyHost;
    private String serverNameSpace;
    private boolean useProxy;
    private String proxyPort;
    private String methodName;
    private String UserName;
    private String Value;



    public connection_WSDLSchemaConnection(
        String Password,        String proxyPassword,        String portName,        String Encoding,        String proxyUser,        boolean needAuth,        String serverName,        String parameters,        int timeOut,        String EndpointURI,        String portNameSpace,        boolean isInputModel,        String WSDL,        String proxyHost,        String serverNameSpace,        boolean useProxy,        String proxyPort,        String methodName,        String UserName,        String Value    ) {
        super(
        );
        this.Password = Password;
        this.proxyPassword = proxyPassword;
        this.portName = portName;
        this.Encoding = Encoding;
        this.proxyUser = proxyUser;
        this.needAuth = needAuth;
        this.serverName = serverName;
        this.parameters = parameters;
        this.timeOut = timeOut;
        this.EndpointURI = EndpointURI;
        this.portNameSpace = portNameSpace;
        this.isInputModel = isInputModel;
        this.WSDL = WSDL;
        this.proxyHost = proxyHost;
        this.serverNameSpace = serverNameSpace;
        this.useProxy = useProxy;
        this.proxyPort = proxyPort;
        this.methodName = methodName;
        this.UserName = UserName;
        this.Value = Value;
    }


    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getProxypassword() {
        return proxyPassword;
    }

    public void setProxypassword(String proxyPassword) {
        this.proxyPassword = proxyPassword;
    }
    public String getPortname() {
        return portName;
    }

    public void setPortname(String portName) {
        this.portName = portName;
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
    public boolean getNeedauth() {
        return needAuth;
    }

    public void setNeedauth(boolean needAuth) {
        this.needAuth = needAuth;
    }
    public String getServername() {
        return serverName;
    }

    public void setServername(String serverName) {
        this.serverName = serverName;
    }
    public String getParameters() {
        return parameters;
    }

    public void setParameters(String parameters) {
        this.parameters = parameters;
    }
    public int getTimeout() {
        return timeOut;
    }

    public void setTimeout(int timeOut) {
        this.timeOut = timeOut;
    }
    public String getEndpointuri() {
        return EndpointURI;
    }

    public void setEndpointuri(String EndpointURI) {
        this.EndpointURI = EndpointURI;
    }
    public String getPortnamespace() {
        return portNameSpace;
    }

    public void setPortnamespace(String portNameSpace) {
        this.portNameSpace = portNameSpace;
    }
    public boolean getIsinputmodel() {
        return isInputModel;
    }

    public void setIsinputmodel(boolean isInputModel) {
        this.isInputModel = isInputModel;
    }
    public String getWsdl() {
        return WSDL;
    }

    public void setWsdl(String WSDL) {
        this.WSDL = WSDL;
    }
    public String getProxyhost() {
        return proxyHost;
    }

    public void setProxyhost(String proxyHost) {
        this.proxyHost = proxyHost;
    }
    public String getServernamespace() {
        return serverNameSpace;
    }

    public void setServernamespace(String serverNameSpace) {
        this.serverNameSpace = serverNameSpace;
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
    public String getUsername() {
        return UserName;
    }

    public void setUsername(String UserName) {
        this.UserName = UserName;
    }
    public String getValue() {
        return Value;
    }

    public void setValue(String Value) {
        this.Value = Value;
    }


}
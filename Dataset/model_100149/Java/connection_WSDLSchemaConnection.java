





import java.util.List;
import java.util.ArrayList;

public class connection_WSDLSchemaConnection extends Connection {

    private String Value;
    private String WSDL;
    private String UserName;
    private String proxyPort;
    private String methodName;
    private int timeOut;
    private boolean isInputModel;
    private boolean useProxy;
    private String proxyUser;
    private String EndpointURI;
    private boolean needAuth;
    private String Encoding;
    private String proxyPassword;
    private String Password;
    private String serverName;
    private String portNameSpace;
    private String serverNameSpace;
    private String proxyHost;
    private String portName;
    private String parameters;



    public connection_WSDLSchemaConnection(
        String Value,        String WSDL,        String UserName,        String proxyPort,        String methodName,        int timeOut,        boolean isInputModel,        boolean useProxy,        String proxyUser,        String EndpointURI,        boolean needAuth,        String Encoding,        String proxyPassword,        String Password,        String serverName,        String portNameSpace,        String serverNameSpace,        String proxyHost,        String portName,        String parameters    ) {
        super(
        );
        this.Value = Value;
        this.WSDL = WSDL;
        this.UserName = UserName;
        this.proxyPort = proxyPort;
        this.methodName = methodName;
        this.timeOut = timeOut;
        this.isInputModel = isInputModel;
        this.useProxy = useProxy;
        this.proxyUser = proxyUser;
        this.EndpointURI = EndpointURI;
        this.needAuth = needAuth;
        this.Encoding = Encoding;
        this.proxyPassword = proxyPassword;
        this.Password = Password;
        this.serverName = serverName;
        this.portNameSpace = portNameSpace;
        this.serverNameSpace = serverNameSpace;
        this.proxyHost = proxyHost;
        this.portName = portName;
        this.parameters = parameters;
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
    public String getUsername() {
        return UserName;
    }

    public void setUsername(String UserName) {
        this.UserName = UserName;
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
    public int getTimeout() {
        return timeOut;
    }

    public void setTimeout(int timeOut) {
        this.timeOut = timeOut;
    }
    public boolean getIsinputmodel() {
        return isInputModel;
    }

    public void setIsinputmodel(boolean isInputModel) {
        this.isInputModel = isInputModel;
    }
    public boolean getUseproxy() {
        return useProxy;
    }

    public void setUseproxy(boolean useProxy) {
        this.useProxy = useProxy;
    }
    public String getProxyuser() {
        return proxyUser;
    }

    public void setProxyuser(String proxyUser) {
        this.proxyUser = proxyUser;
    }
    public String getEndpointuri() {
        return EndpointURI;
    }

    public void setEndpointuri(String EndpointURI) {
        this.EndpointURI = EndpointURI;
    }
    public boolean getNeedauth() {
        return needAuth;
    }

    public void setNeedauth(boolean needAuth) {
        this.needAuth = needAuth;
    }
    public String getEncoding() {
        return Encoding;
    }

    public void setEncoding(String Encoding) {
        this.Encoding = Encoding;
    }
    public String getProxypassword() {
        return proxyPassword;
    }

    public void setProxypassword(String proxyPassword) {
        this.proxyPassword = proxyPassword;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getServername() {
        return serverName;
    }

    public void setServername(String serverName) {
        this.serverName = serverName;
    }
    public String getPortnamespace() {
        return portNameSpace;
    }

    public void setPortnamespace(String portNameSpace) {
        this.portNameSpace = portNameSpace;
    }
    public String getServernamespace() {
        return serverNameSpace;
    }

    public void setServernamespace(String serverNameSpace) {
        this.serverNameSpace = serverNameSpace;
    }
    public String getProxyhost() {
        return proxyHost;
    }

    public void setProxyhost(String proxyHost) {
        this.proxyHost = proxyHost;
    }
    public String getPortname() {
        return portName;
    }

    public void setPortname(String portName) {
        this.portName = portName;
    }
    public String getParameters() {
        return parameters;
    }

    public void setParameters(String parameters) {
        this.parameters = parameters;
    }


}
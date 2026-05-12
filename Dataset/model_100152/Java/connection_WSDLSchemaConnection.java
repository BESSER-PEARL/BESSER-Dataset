





import java.util.List;
import java.util.ArrayList;

public class connection_WSDLSchemaConnection extends Connection {

    private String proxyPort;
    private String Password;
    private String proxyPassword;
    private String methodName;
    private String Encoding;
    private String Value;
    private boolean needAuth;
    private String EndpointURI;
    private String portNameSpace;
    private int timeOut;
    private String serverName;
    private boolean isInputModel;
    private String portName;
    private String parameters;
    private String UserName;
    private String WSDL;
    private String proxyHost;
    private String serverNameSpace;
    private String proxyUser;
    private boolean useProxy;



    public connection_WSDLSchemaConnection(
        String proxyPort,        String Password,        String proxyPassword,        String methodName,        String Encoding,        String Value,        boolean needAuth,        String EndpointURI,        String portNameSpace,        int timeOut,        String serverName,        boolean isInputModel,        String portName,        String parameters,        String UserName,        String WSDL,        String proxyHost,        String serverNameSpace,        String proxyUser,        boolean useProxy    ) {
        super(
        );
        this.proxyPort = proxyPort;
        this.Password = Password;
        this.proxyPassword = proxyPassword;
        this.methodName = methodName;
        this.Encoding = Encoding;
        this.Value = Value;
        this.needAuth = needAuth;
        this.EndpointURI = EndpointURI;
        this.portNameSpace = portNameSpace;
        this.timeOut = timeOut;
        this.serverName = serverName;
        this.isInputModel = isInputModel;
        this.portName = portName;
        this.parameters = parameters;
        this.UserName = UserName;
        this.WSDL = WSDL;
        this.proxyHost = proxyHost;
        this.serverNameSpace = serverNameSpace;
        this.proxyUser = proxyUser;
        this.useProxy = useProxy;
    }


    public String getProxyport() {
        return proxyPort;
    }

    public void setProxyport(String proxyPort) {
        this.proxyPort = proxyPort;
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
    public String getMethodname() {
        return methodName;
    }

    public void setMethodname(String methodName) {
        this.methodName = methodName;
    }
    public String getEncoding() {
        return Encoding;
    }

    public void setEncoding(String Encoding) {
        this.Encoding = Encoding;
    }
    public String getValue() {
        return Value;
    }

    public void setValue(String Value) {
        this.Value = Value;
    }
    public boolean getNeedauth() {
        return needAuth;
    }

    public void setNeedauth(boolean needAuth) {
        this.needAuth = needAuth;
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
    public int getTimeout() {
        return timeOut;
    }

    public void setTimeout(int timeOut) {
        this.timeOut = timeOut;
    }
    public String getServername() {
        return serverName;
    }

    public void setServername(String serverName) {
        this.serverName = serverName;
    }
    public boolean getIsinputmodel() {
        return isInputModel;
    }

    public void setIsinputmodel(boolean isInputModel) {
        this.isInputModel = isInputModel;
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
    public String getUsername() {
        return UserName;
    }

    public void setUsername(String UserName) {
        this.UserName = UserName;
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
    public String getProxyuser() {
        return proxyUser;
    }

    public void setProxyuser(String proxyUser) {
        this.proxyUser = proxyUser;
    }
    public boolean getUseproxy() {
        return useProxy;
    }

    public void setUseproxy(boolean useProxy) {
        this.useProxy = useProxy;
    }


}
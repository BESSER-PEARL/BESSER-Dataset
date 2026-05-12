





import java.util.List;
import java.util.ArrayList;

public class connection_MDMConnection extends Connection {

    private String Port;
    private String Universe;
    private String Server;
    private String Password;
    private String serverUrl;
    private String context;
    private String protocol;
    private String Datacluster;
    private String Username;
    private String Datamodel;



    public connection_MDMConnection(
        String Port,        String Universe,        String Server,        String Password,        String serverUrl,        String context,        String protocol,        String Datacluster,        String Username,        String Datamodel    ) {
        super(
        );
        this.Port = Port;
        this.Universe = Universe;
        this.Server = Server;
        this.Password = Password;
        this.serverUrl = serverUrl;
        this.context = context;
        this.protocol = protocol;
        this.Datacluster = Datacluster;
        this.Username = Username;
        this.Datamodel = Datamodel;
    }


    public String getPort() {
        return Port;
    }

    public void setPort(String Port) {
        this.Port = Port;
    }
    public String getUniverse() {
        return Universe;
    }

    public void setUniverse(String Universe) {
        this.Universe = Universe;
    }
    public String getServer() {
        return Server;
    }

    public void setServer(String Server) {
        this.Server = Server;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getServerurl() {
        return serverUrl;
    }

    public void setServerurl(String serverUrl) {
        this.serverUrl = serverUrl;
    }
    public String getContext() {
        return context;
    }

    public void setContext(String context) {
        this.context = context;
    }
    public String getProtocol() {
        return protocol;
    }

    public void setProtocol(String protocol) {
        this.protocol = protocol;
    }
    public String getDatacluster() {
        return Datacluster;
    }

    public void setDatacluster(String Datacluster) {
        this.Datacluster = Datacluster;
    }
    public String getUsername() {
        return Username;
    }

    public void setUsername(String Username) {
        this.Username = Username;
    }
    public String getDatamodel() {
        return Datamodel;
    }

    public void setDatamodel(String Datamodel) {
        this.Datamodel = Datamodel;
    }


}
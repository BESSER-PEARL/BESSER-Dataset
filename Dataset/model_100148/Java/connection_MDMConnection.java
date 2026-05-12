





import java.util.List;
import java.util.ArrayList;

public class connection_MDMConnection extends Connection {

    private String protocol;
    private String Universe;
    private String Server;
    private String Port;
    private String context;
    private String Datacluster;
    private String Password;
    private String Datamodel;
    private String Username;



    public connection_MDMConnection(
        String protocol,        String Universe,        String Server,        String Port,        String context,        String Datacluster,        String Password,        String Datamodel,        String Username    ) {
        super(
        );
        this.protocol = protocol;
        this.Universe = Universe;
        this.Server = Server;
        this.Port = Port;
        this.context = context;
        this.Datacluster = Datacluster;
        this.Password = Password;
        this.Datamodel = Datamodel;
        this.Username = Username;
    }


    public String getProtocol() {
        return protocol;
    }

    public void setProtocol(String protocol) {
        this.protocol = protocol;
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
    public String getPort() {
        return Port;
    }

    public void setPort(String Port) {
        this.Port = Port;
    }
    public String getContext() {
        return context;
    }

    public void setContext(String context) {
        this.context = context;
    }
    public String getDatacluster() {
        return Datacluster;
    }

    public void setDatacluster(String Datacluster) {
        this.Datacluster = Datacluster;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getDatamodel() {
        return Datamodel;
    }

    public void setDatamodel(String Datamodel) {
        this.Datamodel = Datamodel;
    }
    public String getUsername() {
        return Username;
    }

    public void setUsername(String Username) {
        this.Username = Username;
    }


}
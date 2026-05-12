





import java.util.List;
import java.util.ArrayList;

public class connection_MDMConnection extends Connection {

    private String Datamodel;
    private String Username;
    private String protocol;
    private String Datacluster;
    private String Server;
    private String Password;
    private String Port;
    private String Universe;
    private String context;



    public connection_MDMConnection(
        String Datamodel,        String Username,        String protocol,        String Datacluster,        String Server,        String Password,        String Port,        String Universe,        String context    ) {
        super(
        );
        this.Datamodel = Datamodel;
        this.Username = Username;
        this.protocol = protocol;
        this.Datacluster = Datacluster;
        this.Server = Server;
        this.Password = Password;
        this.Port = Port;
        this.Universe = Universe;
        this.context = context;
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
    public String getContext() {
        return context;
    }

    public void setContext(String context) {
        this.context = context;
    }


}






import java.util.List;
import java.util.ArrayList;

public class connection_MDMConnection extends Connection {

    private String protocol;
    private String Datacluster;
    private String Username;
    private String Password;
    private String Datamodel;
    private String Universe;
    private String context;
    private String Port;
    private String Server;



    public connection_MDMConnection(
        String protocol,        String Datacluster,        String Username,        String Password,        String Datamodel,        String Universe,        String context,        String Port,        String Server    ) {
        super(
        );
        this.protocol = protocol;
        this.Datacluster = Datacluster;
        this.Username = Username;
        this.Password = Password;
        this.Datamodel = Datamodel;
        this.Universe = Universe;
        this.context = context;
        this.Port = Port;
        this.Server = Server;
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
    public String getPort() {
        return Port;
    }

    public void setPort(String Port) {
        this.Port = Port;
    }
    public String getServer() {
        return Server;
    }

    public void setServer(String Server) {
        this.Server = Server;
    }


}
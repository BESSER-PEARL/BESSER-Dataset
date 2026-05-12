





import java.util.List;
import java.util.ArrayList;

public class connection_MDMConnection extends Connection {

    private String Port;
    private String Universe;
    private String Password;
    private String Username;
    private String Datacluster;
    private String Server;
    private String Datamodel;



    public connection_MDMConnection(
        String Port,        String Universe,        String Password,        String Username,        String Datacluster,        String Server,        String Datamodel    ) {
        super(
        );
        this.Port = Port;
        this.Universe = Universe;
        this.Password = Password;
        this.Username = Username;
        this.Datacluster = Datacluster;
        this.Server = Server;
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
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getUsername() {
        return Username;
    }

    public void setUsername(String Username) {
        this.Username = Username;
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
    public String getDatamodel() {
        return Datamodel;
    }

    public void setDatamodel(String Datamodel) {
        this.Datamodel = Datamodel;
    }


}
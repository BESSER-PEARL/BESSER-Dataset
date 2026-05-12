





import java.util.List;
import java.util.ArrayList;

public class connection_MDMConnection extends Connection {

    private String Datamodel;
    private String Password;
    private String Datacluster;
    private String Port;
    private String Username;
    private String Server;
    private String Universe;



    public connection_MDMConnection(
        String Datamodel,        String Password,        String Datacluster,        String Port,        String Username,        String Server,        String Universe    ) {
        super(
        );
        this.Datamodel = Datamodel;
        this.Password = Password;
        this.Datacluster = Datacluster;
        this.Port = Port;
        this.Username = Username;
        this.Server = Server;
        this.Universe = Universe;
    }


    public String getDatamodel() {
        return Datamodel;
    }

    public void setDatamodel(String Datamodel) {
        this.Datamodel = Datamodel;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getDatacluster() {
        return Datacluster;
    }

    public void setDatacluster(String Datacluster) {
        this.Datacluster = Datacluster;
    }
    public String getPort() {
        return Port;
    }

    public void setPort(String Port) {
        this.Port = Port;
    }
    public String getUsername() {
        return Username;
    }

    public void setUsername(String Username) {
        this.Username = Username;
    }
    public String getServer() {
        return Server;
    }

    public void setServer(String Server) {
        this.Server = Server;
    }
    public String getUniverse() {
        return Universe;
    }

    public void setUniverse(String Universe) {
        this.Universe = Universe;
    }


}
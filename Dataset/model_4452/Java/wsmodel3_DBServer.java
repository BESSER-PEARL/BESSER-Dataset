





import java.util.List;
import java.util.ArrayList;

public class wsmodel3_DBServer extends Server {

    private String type;
    private String pass_;
    private int port;
    private String usser;
    private String database;



    public wsmodel3_DBServer(
        String type,        String pass_,        int port,        String usser,        String database    ) {
        super(
        );
        this.type = type;
        this.pass_ = pass_;
        this.port = port;
        this.usser = usser;
        this.database = database;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getPass_() {
        return pass_;
    }

    public void setPass_(String pass_) {
        this.pass_ = pass_;
    }
    public int getPort() {
        return port;
    }

    public void setPort(int port) {
        this.port = port;
    }
    public String getUsser() {
        return usser;
    }

    public void setUsser(String usser) {
        this.usser = usser;
    }
    public String getDatabase() {
        return database;
    }

    public void setDatabase(String database) {
        this.database = database;
    }


}
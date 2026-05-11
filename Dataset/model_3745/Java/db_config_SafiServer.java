





import java.util.List;
import java.util.ArrayList;

public class db_config_SafiServer extends ServerResource {

    private boolean debug;
    private int dbPort;
    private String bindIP;
    private boolean running;
    private int managementPort;





    private List<config_User> config_users;




    private config_User config_user;


    public db_config_SafiServer(
        boolean debug,        int dbPort,        String bindIP,        boolean running,        int managementPort    ) {
        super(
        );
        this.debug = debug;
        this.dbPort = dbPort;
        this.bindIP = bindIP;
        this.running = running;
        this.managementPort = managementPort;
        this.config_users = new ArrayList<>();
    }

    public db_config_SafiServer(
        boolean debug,        int dbPort,        String bindIP,        boolean running,        int managementPort        ArrayList<config_User> config_users    ) {
        this.debug = debug;
        this.dbPort = dbPort;
        this.bindIP = bindIP;
        this.running = running;
        this.managementPort = managementPort;
        this.config_users = config_users;
    }

    public boolean getDebug() {
        return debug;
    }

    public void setDebug(boolean debug) {
        this.debug = debug;
    }
    public int getDbport() {
        return dbPort;
    }

    public void setDbport(int dbPort) {
        this.dbPort = dbPort;
    }
    public String getBindip() {
        return bindIP;
    }

    public void setBindip(String bindIP) {
        this.bindIP = bindIP;
    }
    public boolean getRunning() {
        return running;
    }

    public void setRunning(boolean running) {
        this.running = running;
    }
    public int getManagementport() {
        return managementPort;
    }

    public void setManagementport(int managementPort) {
        this.managementPort = managementPort;
    }

    public List<config_User> getConfig_users() {
        return config_users;
    }

    public void addConfig_user(Config_user config_user) {
        this.config_users.add(config_user);
    }
    public config_User getConfig_user() {
        return config_user;
    }

    public void setConfig_user(config_User config_user) {
        this.config_user = config_user;
    }

}
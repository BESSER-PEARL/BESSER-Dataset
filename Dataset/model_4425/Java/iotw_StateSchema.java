





import java.util.List;
import java.util.ArrayList;

public class iotw_StateSchema  {






    private List<iotw_StateControl> iotw_statecontrols;




    private List<iotw_Connection> iotw_connections;




    private iotw_Connection iotw_connection;


    public iotw_StateSchema(
    ) {
        this.iotw_statecontrols = new ArrayList<>();
        this.iotw_connections = new ArrayList<>();
    }

    public iotw_StateSchema(
        ArrayList<iotw_StateControl> iotw_statecontrols,        ArrayList<iotw_Connection> iotw_connections    ) {
        this.iotw_statecontrols = iotw_statecontrols;
        this.iotw_connections = iotw_connections;
    }


    public List<iotw_StateControl> getIotw_statecontrols() {
        return iotw_statecontrols;
    }

    public void addIotw_statecontrol(Iotw_statecontrol iotw_statecontrol) {
        this.iotw_statecontrols.add(iotw_statecontrol);
    }
    public List<iotw_Connection> getIotw_connections() {
        return iotw_connections;
    }

    public void addIotw_connection(Iotw_connection iotw_connection) {
        this.iotw_connections.add(iotw_connection);
    }
    public iotw_Connection getIotw_connection() {
        return iotw_connection;
    }

    public void setIotw_connection(iotw_Connection iotw_connection) {
        this.iotw_connection = iotw_connection;
    }

}
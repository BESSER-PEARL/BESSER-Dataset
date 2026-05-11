





import java.util.List;
import java.util.ArrayList;

public class iotw_StateComponent extends Component {

    private String name;





    private List<iotw_Connection> iotw_connections;




    private List<iotw_Connection> iotw_connections;




    private iotw_StateSchema iotw_stateschema;


    public iotw_StateComponent(
        String name    ) {
        super(
        );
        this.name = name;
        this.iotw_connections = new ArrayList<>();
        this.iotw_connections = new ArrayList<>();
    }

    public iotw_StateComponent(
        String name        ArrayList<iotw_Connection> iotw_connections,        ArrayList<iotw_Connection> iotw_connections    ) {
        this.name = name;
        this.iotw_connections = iotw_connections;
        this.iotw_connections = iotw_connections;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<iotw_Connection> getIotw_connections() {
        return iotw_connections;
    }

    public void addIotw_connection(Iotw_connection iotw_connection) {
        this.iotw_connections.add(iotw_connection);
    }
    public List<iotw_Connection> getIotw_connections() {
        return iotw_connections;
    }

    public void addIotw_connection(Iotw_connection iotw_connection) {
        this.iotw_connections.add(iotw_connection);
    }
    public iotw_StateSchema getIotw_stateschema() {
        return iotw_stateschema;
    }

    public void setIotw_stateschema(iotw_StateSchema iotw_stateschema) {
        this.iotw_stateschema = iotw_stateschema;
    }

}
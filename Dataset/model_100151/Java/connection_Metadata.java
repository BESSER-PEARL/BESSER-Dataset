





import java.util.List;
import java.util.ArrayList;

public class connection_Metadata extends AbstractMetadataObject {






    private List<connection_Connection> connection_connections;


    public connection_Metadata(
    ) {
        super(
        );
        this.connection_connections = new ArrayList<>();
    }

    public connection_Metadata(
        ArrayList<connection_Connection> connection_connections    ) {
        this.connection_connections = connection_connections;
    }


    public List<connection_Connection> getConnection_connections() {
        return connection_connections;
    }

    public void addConnection_connection(Connection_connection connection_connection) {
        this.connection_connections.add(connection_connection);
    }

}
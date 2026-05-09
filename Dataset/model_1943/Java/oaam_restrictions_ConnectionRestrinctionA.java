





import java.util.List;
import java.util.ArrayList;

public class oaam_restrictions_ConnectionRestrinctionA  {






    private List<Connection> connections;


    public oaam_restrictions_ConnectionRestrinctionA(
    ) {
        this.connections = new ArrayList<>();
    }

    public oaam_restrictions_ConnectionRestrinctionA(
        ArrayList<Connection> connections    ) {
        this.connections = connections;
    }


    public List<Connection> getConnections() {
        return connections;
    }

    public void addConnection(Connection connection) {
        this.connections.add(connection);
    }

}
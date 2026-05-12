





import java.util.List;
import java.util.ArrayList;

public class connection_QueriesConnection  {






    private connection_Connection connection_connection;




    private connection_Connection connection_connection;




    private connection_Query connection_query;




    private List<connection_Query> connection_querys;


    public connection_QueriesConnection(
    ) {
        this.connection_querys = new ArrayList<>();
    }

    public connection_QueriesConnection(
        ArrayList<connection_Query> connection_querys    ) {
        this.connection_querys = connection_querys;
    }


    public connection_Connection getConnection_connection() {
        return connection_connection;
    }

    public void setConnection_connection(connection_Connection connection_connection) {
        this.connection_connection = connection_connection;
    }
    public connection_Connection getConnection_connection() {
        return connection_connection;
    }

    public void setConnection_connection(connection_Connection connection_connection) {
        this.connection_connection = connection_connection;
    }
    public connection_Query getConnection_query() {
        return connection_query;
    }

    public void setConnection_query(connection_Query connection_query) {
        this.connection_query = connection_query;
    }
    public List<connection_Query> getConnection_querys() {
        return connection_querys;
    }

    public void addConnection_query(Connection_query connection_query) {
        this.connection_querys.add(connection_query);
    }

}
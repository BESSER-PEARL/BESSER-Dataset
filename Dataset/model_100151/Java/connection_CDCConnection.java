





import java.util.List;
import java.util.ArrayList;

public class connection_CDCConnection  {






    private List<connection_CDCType> connection_cdctypes;




    private connection_CDCType connection_cdctype;




    private connection_DatabaseConnection connection_databaseconnection;




    private connection_DatabaseConnection connection_databaseconnection;


    public connection_CDCConnection(
    ) {
        this.connection_cdctypes = new ArrayList<>();
    }

    public connection_CDCConnection(
        ArrayList<connection_CDCType> connection_cdctypes    ) {
        this.connection_cdctypes = connection_cdctypes;
    }


    public List<connection_CDCType> getConnection_cdctypes() {
        return connection_cdctypes;
    }

    public void addConnection_cdctype(Connection_cdctype connection_cdctype) {
        this.connection_cdctypes.add(connection_cdctype);
    }
    public connection_CDCType getConnection_cdctype() {
        return connection_cdctype;
    }

    public void setConnection_cdctype(connection_CDCType connection_cdctype) {
        this.connection_cdctype = connection_cdctype;
    }
    public connection_DatabaseConnection getConnection_databaseconnection() {
        return connection_databaseconnection;
    }

    public void setConnection_databaseconnection(connection_DatabaseConnection connection_databaseconnection) {
        this.connection_databaseconnection = connection_databaseconnection;
    }
    public connection_DatabaseConnection getConnection_databaseconnection() {
        return connection_databaseconnection;
    }

    public void setConnection_databaseconnection(connection_DatabaseConnection connection_databaseconnection) {
        this.connection_databaseconnection = connection_databaseconnection;
    }

}
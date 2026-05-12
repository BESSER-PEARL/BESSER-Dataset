





import java.util.List;
import java.util.ArrayList;

public class connection_SAPConnection extends Connection {

    private String Username;
    private String SystemNumber;
    private String Password;
    private String Host;
    private String currentFucntion;
    private String Language;
    private String Client;





    private List<connection_SAPFunctionUnit> connection_sapfunctionunits;




    private connection_SAPFunctionUnit connection_sapfunctionunit;


    public connection_SAPConnection(
        String Username,        String SystemNumber,        String Password,        String Host,        String currentFucntion,        String Language,        String Client    ) {
        super(
        );
        this.Username = Username;
        this.SystemNumber = SystemNumber;
        this.Password = Password;
        this.Host = Host;
        this.currentFucntion = currentFucntion;
        this.Language = Language;
        this.Client = Client;
        this.connection_sapfunctionunits = new ArrayList<>();
    }

    public connection_SAPConnection(
        String Username,        String SystemNumber,        String Password,        String Host,        String currentFucntion,        String Language,        String Client        ArrayList<connection_SAPFunctionUnit> connection_sapfunctionunits    ) {
        this.Username = Username;
        this.SystemNumber = SystemNumber;
        this.Password = Password;
        this.Host = Host;
        this.currentFucntion = currentFucntion;
        this.Language = Language;
        this.Client = Client;
        this.connection_sapfunctionunits = connection_sapfunctionunits;
    }

    public String getUsername() {
        return Username;
    }

    public void setUsername(String Username) {
        this.Username = Username;
    }
    public String getSystemnumber() {
        return SystemNumber;
    }

    public void setSystemnumber(String SystemNumber) {
        this.SystemNumber = SystemNumber;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getHost() {
        return Host;
    }

    public void setHost(String Host) {
        this.Host = Host;
    }
    public String getCurrentfucntion() {
        return currentFucntion;
    }

    public void setCurrentfucntion(String currentFucntion) {
        this.currentFucntion = currentFucntion;
    }
    public String getLanguage() {
        return Language;
    }

    public void setLanguage(String Language) {
        this.Language = Language;
    }
    public String getClient() {
        return Client;
    }

    public void setClient(String Client) {
        this.Client = Client;
    }

    public List<connection_SAPFunctionUnit> getConnection_sapfunctionunits() {
        return connection_sapfunctionunits;
    }

    public void addConnection_sapfunctionunit(Connection_sapfunctionunit connection_sapfunctionunit) {
        this.connection_sapfunctionunits.add(connection_sapfunctionunit);
    }
    public connection_SAPFunctionUnit getConnection_sapfunctionunit() {
        return connection_sapfunctionunit;
    }

    public void setConnection_sapfunctionunit(connection_SAPFunctionUnit connection_sapfunctionunit) {
        this.connection_sapfunctionunit = connection_sapfunctionunit;
    }

}
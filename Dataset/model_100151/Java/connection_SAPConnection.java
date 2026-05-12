





import java.util.List;
import java.util.ArrayList;

public class connection_SAPConnection extends Connection {

    private String SystemNumber;
    private String Client;
    private String Password;
    private String currentFucntion;
    private String Host;
    private String Language;
    private String Username;





    private connection_SAPFunctionUnit connection_sapfunctionunit;




    private List<connection_SAPFunctionUnit> connection_sapfunctionunits;


    public connection_SAPConnection(
        String SystemNumber,        String Client,        String Password,        String currentFucntion,        String Host,        String Language,        String Username    ) {
        super(
        );
        this.SystemNumber = SystemNumber;
        this.Client = Client;
        this.Password = Password;
        this.currentFucntion = currentFucntion;
        this.Host = Host;
        this.Language = Language;
        this.Username = Username;
        this.connection_sapfunctionunits = new ArrayList<>();
    }

    public connection_SAPConnection(
        String SystemNumber,        String Client,        String Password,        String currentFucntion,        String Host,        String Language,        String Username        ArrayList<connection_SAPFunctionUnit> connection_sapfunctionunits    ) {
        this.SystemNumber = SystemNumber;
        this.Client = Client;
        this.Password = Password;
        this.currentFucntion = currentFucntion;
        this.Host = Host;
        this.Language = Language;
        this.Username = Username;
        this.connection_sapfunctionunits = connection_sapfunctionunits;
    }

    public String getSystemnumber() {
        return SystemNumber;
    }

    public void setSystemnumber(String SystemNumber) {
        this.SystemNumber = SystemNumber;
    }
    public String getClient() {
        return Client;
    }

    public void setClient(String Client) {
        this.Client = Client;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getCurrentfucntion() {
        return currentFucntion;
    }

    public void setCurrentfucntion(String currentFucntion) {
        this.currentFucntion = currentFucntion;
    }
    public String getHost() {
        return Host;
    }

    public void setHost(String Host) {
        this.Host = Host;
    }
    public String getLanguage() {
        return Language;
    }

    public void setLanguage(String Language) {
        this.Language = Language;
    }
    public String getUsername() {
        return Username;
    }

    public void setUsername(String Username) {
        this.Username = Username;
    }

    public connection_SAPFunctionUnit getConnection_sapfunctionunit() {
        return connection_sapfunctionunit;
    }

    public void setConnection_sapfunctionunit(connection_SAPFunctionUnit connection_sapfunctionunit) {
        this.connection_sapfunctionunit = connection_sapfunctionunit;
    }
    public List<connection_SAPFunctionUnit> getConnection_sapfunctionunits() {
        return connection_sapfunctionunits;
    }

    public void addConnection_sapfunctionunit(Connection_sapfunctionunit connection_sapfunctionunit) {
        this.connection_sapfunctionunits.add(connection_sapfunctionunit);
    }

}
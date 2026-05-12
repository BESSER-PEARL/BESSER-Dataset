





import java.util.List;
import java.util.ArrayList;

public class connection_SAPConnection extends Connection {

    private String Language;
    private String Password;
    private String Username;
    private String Client;
    private String SystemNumber;
    private String Host;
    private String currentFucntion;





    private List<connection_SAPFunctionUnit> connection_sapfunctionunits;




    private connection_SAPFunctionUnit connection_sapfunctionunit;


    public connection_SAPConnection(
        String Language,        String Password,        String Username,        String Client,        String SystemNumber,        String Host,        String currentFucntion    ) {
        super(
        );
        this.Language = Language;
        this.Password = Password;
        this.Username = Username;
        this.Client = Client;
        this.SystemNumber = SystemNumber;
        this.Host = Host;
        this.currentFucntion = currentFucntion;
        this.connection_sapfunctionunits = new ArrayList<>();
    }

    public connection_SAPConnection(
        String Language,        String Password,        String Username,        String Client,        String SystemNumber,        String Host,        String currentFucntion        ArrayList<connection_SAPFunctionUnit> connection_sapfunctionunits    ) {
        this.Language = Language;
        this.Password = Password;
        this.Username = Username;
        this.Client = Client;
        this.SystemNumber = SystemNumber;
        this.Host = Host;
        this.currentFucntion = currentFucntion;
        this.connection_sapfunctionunits = connection_sapfunctionunits;
    }

    public String getLanguage() {
        return Language;
    }

    public void setLanguage(String Language) {
        this.Language = Language;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getUsername() {
        return Username;
    }

    public void setUsername(String Username) {
        this.Username = Username;
    }
    public String getClient() {
        return Client;
    }

    public void setClient(String Client) {
        this.Client = Client;
    }
    public String getSystemnumber() {
        return SystemNumber;
    }

    public void setSystemnumber(String SystemNumber) {
        this.SystemNumber = SystemNumber;
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
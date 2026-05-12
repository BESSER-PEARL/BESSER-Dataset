





import java.util.List;
import java.util.ArrayList;

public class connection_SAPConnection extends Connection {

    private String Username;
    private String SystemNumber;
    private String currentFucntion;
    private String Client;
    private String Password;
    private String Host;
    private String Language;





    private connection_SAPIDocUnit connection_sapidocunit;




    private List<connection_SAPFunctionUnit> connection_sapfunctionunits;




    private connection_SAPFunctionUnit connection_sapfunctionunit;




    private List<connection_SAPIDocUnit> connection_sapidocunits;


    public connection_SAPConnection(
        String Username,        String SystemNumber,        String currentFucntion,        String Client,        String Password,        String Host,        String Language    ) {
        super(
        );
        this.Username = Username;
        this.SystemNumber = SystemNumber;
        this.currentFucntion = currentFucntion;
        this.Client = Client;
        this.Password = Password;
        this.Host = Host;
        this.Language = Language;
        this.connection_sapfunctionunits = new ArrayList<>();
        this.connection_sapidocunits = new ArrayList<>();
    }

    public connection_SAPConnection(
        String Username,        String SystemNumber,        String currentFucntion,        String Client,        String Password,        String Host,        String Language        ArrayList<connection_SAPFunctionUnit> connection_sapfunctionunits,        ArrayList<connection_SAPIDocUnit> connection_sapidocunits    ) {
        this.Username = Username;
        this.SystemNumber = SystemNumber;
        this.currentFucntion = currentFucntion;
        this.Client = Client;
        this.Password = Password;
        this.Host = Host;
        this.Language = Language;
        this.connection_sapfunctionunits = connection_sapfunctionunits;
        this.connection_sapidocunits = connection_sapidocunits;
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
    public String getCurrentfucntion() {
        return currentFucntion;
    }

    public void setCurrentfucntion(String currentFucntion) {
        this.currentFucntion = currentFucntion;
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

    public connection_SAPIDocUnit getConnection_sapidocunit() {
        return connection_sapidocunit;
    }

    public void setConnection_sapidocunit(connection_SAPIDocUnit connection_sapidocunit) {
        this.connection_sapidocunit = connection_sapidocunit;
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
    public List<connection_SAPIDocUnit> getConnection_sapidocunits() {
        return connection_sapidocunits;
    }

    public void addConnection_sapidocunit(Connection_sapidocunit connection_sapidocunit) {
        this.connection_sapidocunits.add(connection_sapidocunit);
    }

}
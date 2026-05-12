





import java.util.List;
import java.util.ArrayList;

public class connection_SAPConnection extends Connection {

    private String Client;
    private String Host;
    private String SystemNumber;
    private String Username;
    private String Language;
    private String currentFucntion;
    private String Password;
    private String jcoVersion;





    private connection_SAPIDocUnit connection_sapidocunit;




    private List<connection_SAPIDocUnit> connection_sapidocunits;




    private List<connection_SAPFunctionUnit> connection_sapfunctionunits;




    private connection_SAPFunctionUnit connection_sapfunctionunit;


    public connection_SAPConnection(
        String Client,        String Host,        String SystemNumber,        String Username,        String Language,        String currentFucntion,        String Password,        String jcoVersion    ) {
        super(
        );
        this.Client = Client;
        this.Host = Host;
        this.SystemNumber = SystemNumber;
        this.Username = Username;
        this.Language = Language;
        this.currentFucntion = currentFucntion;
        this.Password = Password;
        this.jcoVersion = jcoVersion;
        this.connection_sapidocunits = new ArrayList<>();
        this.connection_sapfunctionunits = new ArrayList<>();
    }

    public connection_SAPConnection(
        String Client,        String Host,        String SystemNumber,        String Username,        String Language,        String currentFucntion,        String Password,        String jcoVersion        ArrayList<connection_SAPIDocUnit> connection_sapidocunits,        ArrayList<connection_SAPFunctionUnit> connection_sapfunctionunits    ) {
        this.Client = Client;
        this.Host = Host;
        this.SystemNumber = SystemNumber;
        this.Username = Username;
        this.Language = Language;
        this.currentFucntion = currentFucntion;
        this.Password = Password;
        this.jcoVersion = jcoVersion;
        this.connection_sapidocunits = connection_sapidocunits;
        this.connection_sapfunctionunits = connection_sapfunctionunits;
    }

    public String getClient() {
        return Client;
    }

    public void setClient(String Client) {
        this.Client = Client;
    }
    public String getHost() {
        return Host;
    }

    public void setHost(String Host) {
        this.Host = Host;
    }
    public String getSystemnumber() {
        return SystemNumber;
    }

    public void setSystemnumber(String SystemNumber) {
        this.SystemNumber = SystemNumber;
    }
    public String getUsername() {
        return Username;
    }

    public void setUsername(String Username) {
        this.Username = Username;
    }
    public String getLanguage() {
        return Language;
    }

    public void setLanguage(String Language) {
        this.Language = Language;
    }
    public String getCurrentfucntion() {
        return currentFucntion;
    }

    public void setCurrentfucntion(String currentFucntion) {
        this.currentFucntion = currentFucntion;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getJcoversion() {
        return jcoVersion;
    }

    public void setJcoversion(String jcoVersion) {
        this.jcoVersion = jcoVersion;
    }

    public connection_SAPIDocUnit getConnection_sapidocunit() {
        return connection_sapidocunit;
    }

    public void setConnection_sapidocunit(connection_SAPIDocUnit connection_sapidocunit) {
        this.connection_sapidocunit = connection_sapidocunit;
    }
    public List<connection_SAPIDocUnit> getConnection_sapidocunits() {
        return connection_sapidocunits;
    }

    public void addConnection_sapidocunit(Connection_sapidocunit connection_sapidocunit) {
        this.connection_sapidocunits.add(connection_sapidocunit);
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
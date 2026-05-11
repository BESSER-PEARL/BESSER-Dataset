





import java.util.List;
import java.util.ArrayList;

public class ingest_Database  {

    private String jdbcUrl;
    private String jdbcPassword;
    private String jdbcUser;
    private String jdbcDriver;
    private String label;





    private ingest_Catalogue ingest_catalogue;




    private List<ingest_DbSchema> ingest_dbschemas;


    public ingest_Database(
        String jdbcUrl,        String jdbcPassword,        String jdbcUser,        String jdbcDriver,        String label    ) {
        this.jdbcUrl = jdbcUrl;
        this.jdbcPassword = jdbcPassword;
        this.jdbcUser = jdbcUser;
        this.jdbcDriver = jdbcDriver;
        this.label = label;
        this.ingest_dbschemas = new ArrayList<>();
    }

    public ingest_Database(
        String jdbcUrl,        String jdbcPassword,        String jdbcUser,        String jdbcDriver,        String label        ArrayList<ingest_DbSchema> ingest_dbschemas    ) {
        this.jdbcUrl = jdbcUrl;
        this.jdbcPassword = jdbcPassword;
        this.jdbcUser = jdbcUser;
        this.jdbcDriver = jdbcDriver;
        this.label = label;
        this.ingest_dbschemas = ingest_dbschemas;
    }

    public String getJdbcurl() {
        return jdbcUrl;
    }

    public void setJdbcurl(String jdbcUrl) {
        this.jdbcUrl = jdbcUrl;
    }
    public String getJdbcpassword() {
        return jdbcPassword;
    }

    public void setJdbcpassword(String jdbcPassword) {
        this.jdbcPassword = jdbcPassword;
    }
    public String getJdbcuser() {
        return jdbcUser;
    }

    public void setJdbcuser(String jdbcUser) {
        this.jdbcUser = jdbcUser;
    }
    public String getJdbcdriver() {
        return jdbcDriver;
    }

    public void setJdbcdriver(String jdbcDriver) {
        this.jdbcDriver = jdbcDriver;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public ingest_Catalogue getIngest_catalogue() {
        return ingest_catalogue;
    }

    public void setIngest_catalogue(ingest_Catalogue ingest_catalogue) {
        this.ingest_catalogue = ingest_catalogue;
    }
    public List<ingest_DbSchema> getIngest_dbschemas() {
        return ingest_dbschemas;
    }

    public void addIngest_dbschema(Ingest_dbschema ingest_dbschema) {
        this.ingest_dbschemas.add(ingest_dbschema);
    }

}
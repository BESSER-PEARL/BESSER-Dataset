





import java.util.List;
import java.util.ArrayList;

public class ingest_DbTable  {

    private String name;





    private ingest_DbSchema ingest_dbschema;




    private List<ingest_SqoopImport> ingest_sqoopimports;


    public ingest_DbTable(
        String name    ) {
        this.name = name;
        this.ingest_sqoopimports = new ArrayList<>();
    }

    public ingest_DbTable(
        String name        ArrayList<ingest_SqoopImport> ingest_sqoopimports    ) {
        this.name = name;
        this.ingest_sqoopimports = ingest_sqoopimports;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ingest_DbSchema getIngest_dbschema() {
        return ingest_dbschema;
    }

    public void setIngest_dbschema(ingest_DbSchema ingest_dbschema) {
        this.ingest_dbschema = ingest_dbschema;
    }
    public List<ingest_SqoopImport> getIngest_sqoopimports() {
        return ingest_sqoopimports;
    }

    public void addIngest_sqoopimport(Ingest_sqoopimport ingest_sqoopimport) {
        this.ingest_sqoopimports.add(ingest_sqoopimport);
    }

}
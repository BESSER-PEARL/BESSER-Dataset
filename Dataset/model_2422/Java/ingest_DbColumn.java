





import java.util.List;
import java.util.ArrayList;

public class ingest_DbColumn  {

    private String name;
    private int jdbcType;
    private int jdbcPrecision;
    private int jdbcScale;





    private ingest_SqoopHiveIncrementalImport ingest_sqoophiveincrementalimport;




    private ingest_DbTable ingest_dbtable;


    public ingest_DbColumn(
        String name,        int jdbcType,        int jdbcPrecision,        int jdbcScale    ) {
        this.name = name;
        this.jdbcType = jdbcType;
        this.jdbcPrecision = jdbcPrecision;
        this.jdbcScale = jdbcScale;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getJdbctype() {
        return jdbcType;
    }

    public void setJdbctype(int jdbcType) {
        this.jdbcType = jdbcType;
    }
    public int getJdbcprecision() {
        return jdbcPrecision;
    }

    public void setJdbcprecision(int jdbcPrecision) {
        this.jdbcPrecision = jdbcPrecision;
    }
    public int getJdbcscale() {
        return jdbcScale;
    }

    public void setJdbcscale(int jdbcScale) {
        this.jdbcScale = jdbcScale;
    }

    public ingest_SqoopHiveIncrementalImport getIngest_sqoophiveincrementalimport() {
        return ingest_sqoophiveincrementalimport;
    }

    public void setIngest_sqoophiveincrementalimport(ingest_SqoopHiveIncrementalImport ingest_sqoophiveincrementalimport) {
        this.ingest_sqoophiveincrementalimport = ingest_sqoophiveincrementalimport;
    }
    public ingest_DbTable getIngest_dbtable() {
        return ingest_dbtable;
    }

    public void setIngest_dbtable(ingest_DbTable ingest_dbtable) {
        this.ingest_dbtable = ingest_dbtable;
    }

}
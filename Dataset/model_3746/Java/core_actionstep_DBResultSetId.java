





import java.util.List;
import java.util.ArrayList;

public class core_actionstep_DBResultSetId extends ThreadSensitive {

    private String jDBCResultSet;
    private String id;
    private String name;



    public core_actionstep_DBResultSetId(
        String jDBCResultSet,        String id,        String name    ) {
        super(
        );
        this.jDBCResultSet = jDBCResultSet;
        this.id = id;
        this.name = name;
    }


    public String getJdbcresultset() {
        return jDBCResultSet;
    }

    public void setJdbcresultset(String jDBCResultSet) {
        this.jDBCResultSet = jDBCResultSet;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}
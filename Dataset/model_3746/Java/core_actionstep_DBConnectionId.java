





import java.util.List;
import java.util.ArrayList;

public class core_actionstep_DBConnectionId extends ThreadSensitive {

    private String id;
    private String jdbcConnection;



    public core_actionstep_DBConnectionId(
        String id,        String jdbcConnection    ) {
        super(
        );
        this.id = id;
        this.jdbcConnection = jdbcConnection;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getJdbcconnection() {
        return jdbcConnection;
    }

    public void setJdbcconnection(String jdbcConnection) {
        this.jdbcConnection = jdbcConnection;
    }


}
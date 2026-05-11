





import java.util.List;
import java.util.ArrayList;

public class core_actionstep_DBQueryId extends ThreadSensitive {

    private String jdbcStatement;
    private String id;



    public core_actionstep_DBQueryId(
        String jdbcStatement,        String id    ) {
        super(
        );
        this.jdbcStatement = jdbcStatement;
        this.id = id;
    }


    public String getJdbcstatement() {
        return jdbcStatement;
    }

    public void setJdbcstatement(String jdbcStatement) {
        this.jdbcStatement = jdbcStatement;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}
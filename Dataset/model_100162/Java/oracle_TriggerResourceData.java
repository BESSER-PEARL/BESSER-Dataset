





import java.util.List;
import java.util.ArrayList;

public class oracle_TriggerResourceData extends DatabaseResourceData {

    private String sql;



    public oracle_TriggerResourceData(
        String sql    ) {
        super(
        );
        this.sql = sql;
    }


    public String getSql() {
        return sql;
    }

    public void setSql(String sql) {
        this.sql = sql;
    }


}






import java.util.List;
import java.util.ArrayList;

public class database_ViewResourceData extends DatabaseResourceData {

    private boolean isHistory;
    private String sql;



    public database_ViewResourceData(
        boolean isHistory,        String sql    ) {
        super(
        );
        this.isHistory = isHistory;
        this.sql = sql;
    }


    public boolean getIshistory() {
        return isHistory;
    }

    public void setIshistory(boolean isHistory) {
        this.isHistory = isHistory;
    }
    public String getSql() {
        return sql;
    }

    public void setSql(String sql) {
        this.sql = sql;
    }


}
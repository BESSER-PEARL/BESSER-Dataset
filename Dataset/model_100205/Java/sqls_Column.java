





import java.util.List;
import java.util.ArrayList;

public class sqls_Column  {

    private boolean primaryKey;
    private boolean null;
    private String name;





    private sqls_Table sqls_table;


    public sqls_Column(
        boolean primaryKey,        boolean null,        String name    ) {
        this.primaryKey = primaryKey;
        this.null = null;
        this.name = name;
    }


    public boolean getPrimarykey() {
        return primaryKey;
    }

    public void setPrimarykey(boolean primaryKey) {
        this.primaryKey = primaryKey;
    }
    public boolean getNull() {
        return null;
    }

    public void setNull(boolean null) {
        this.null = null;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public sqls_Table getSqls_table() {
        return sqls_table;
    }

    public void setSqls_table(sqls_Table sqls_table) {
        this.sqls_table = sqls_table;
    }

}
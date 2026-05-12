





import java.util.List;
import java.util.ArrayList;

public class database_ForeignKey  {

    private String tableName;
    private String fieldName;





    private database_TableColumn database_tablecolumn;


    public database_ForeignKey(
        String tableName,        String fieldName    ) {
        this.tableName = tableName;
        this.fieldName = fieldName;
    }


    public String getTablename() {
        return tableName;
    }

    public void setTablename(String tableName) {
        this.tableName = tableName;
    }
    public String getFieldname() {
        return fieldName;
    }

    public void setFieldname(String fieldName) {
        this.fieldName = fieldName;
    }

    public database_TableColumn getDatabase_tablecolumn() {
        return database_tablecolumn;
    }

    public void setDatabase_tablecolumn(database_TableColumn database_tablecolumn) {
        this.database_tablecolumn = database_tablecolumn;
    }

}
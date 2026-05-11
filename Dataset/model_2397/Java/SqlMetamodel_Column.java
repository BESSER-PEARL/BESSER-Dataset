





import java.util.List;
import java.util.ArrayList;

public class SqlMetamodel_Column  {

    private String name;
    private String type;
    private boolean nullable;





    private SqlMetamodel_Table sqlmetamodel_table;


    public SqlMetamodel_Column(
        String name,        String type,        boolean nullable    ) {
        this.name = name;
        this.type = type;
        this.nullable = nullable;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public boolean getNullable() {
        return nullable;
    }

    public void setNullable(boolean nullable) {
        this.nullable = nullable;
    }

    public SqlMetamodel_Table getSqlmetamodel_table() {
        return sqlmetamodel_table;
    }

    public void setSqlmetamodel_table(SqlMetamodel_Table sqlmetamodel_table) {
        this.sqlmetamodel_table = sqlmetamodel_table;
    }

}
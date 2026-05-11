





import java.util.List;
import java.util.ArrayList;

public class SqlMetamodel_Table  {

    private String name;





    private SqlMetamodel_Schema sqlmetamodel_schema;


    public SqlMetamodel_Table(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public SqlMetamodel_Schema getSqlmetamodel_schema() {
        return sqlmetamodel_schema;
    }

    public void setSqlmetamodel_schema(SqlMetamodel_Schema sqlmetamodel_schema) {
        this.sqlmetamodel_schema = sqlmetamodel_schema;
    }

}






import java.util.List;
import java.util.ArrayList;

public class SqlMetamodel_Constraint  {

    private String name;





    private SqlMetamodel_Table sqlmetamodel_table;


    public SqlMetamodel_Constraint(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public SqlMetamodel_Table getSqlmetamodel_table() {
        return sqlmetamodel_table;
    }

    public void setSqlmetamodel_table(SqlMetamodel_Table sqlmetamodel_table) {
        this.sqlmetamodel_table = sqlmetamodel_table;
    }

}
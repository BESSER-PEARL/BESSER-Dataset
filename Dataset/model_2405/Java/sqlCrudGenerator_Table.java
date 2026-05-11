





import java.util.List;
import java.util.ArrayList;

public class sqlCrudGenerator_Table  {

    private String name;





    private sqlCrudGenerator_Schema sqlcrudgenerator_schema;


    public sqlCrudGenerator_Table(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public sqlCrudGenerator_Schema getSqlcrudgenerator_schema() {
        return sqlcrudgenerator_schema;
    }

    public void setSqlcrudgenerator_schema(sqlCrudGenerator_Schema sqlcrudgenerator_schema) {
        this.sqlcrudgenerator_schema = sqlcrudgenerator_schema;
    }

}
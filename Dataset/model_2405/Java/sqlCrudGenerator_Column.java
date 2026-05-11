





import java.util.List;
import java.util.ArrayList;

public class sqlCrudGenerator_Column  {

    private String name;





    private sqlCrudGenerator_Table sqlcrudgenerator_table;


    public sqlCrudGenerator_Column(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public sqlCrudGenerator_Table getSqlcrudgenerator_table() {
        return sqlcrudgenerator_table;
    }

    public void setSqlcrudgenerator_table(sqlCrudGenerator_Table sqlcrudgenerator_table) {
        this.sqlcrudgenerator_table = sqlcrudgenerator_table;
    }

}
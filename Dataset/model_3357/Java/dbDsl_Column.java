





import java.util.List;
import java.util.ArrayList;

public class dbDsl_Column  {

    private String name;





    private dbDsl_Table dbdsl_table;


    public dbDsl_Column(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dbDsl_Table getDbdsl_table() {
        return dbdsl_table;
    }

    public void setDbdsl_table(dbDsl_Table dbdsl_table) {
        this.dbdsl_table = dbdsl_table;
    }

}
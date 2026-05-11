





import java.util.List;
import java.util.ArrayList;

public class SQL2003_V2_View extends DerivedTable {






    private SQL2003_V2_Table sql2003_v2_table;




    private List<SQL2003_V2_Table> sql2003_v2_tables;


    public SQL2003_V2_View(
    ) {
        super(
        );
        this.sql2003_v2_tables = new ArrayList<>();
    }

    public SQL2003_V2_View(
        ArrayList<SQL2003_V2_Table> sql2003_v2_tables    ) {
        this.sql2003_v2_tables = sql2003_v2_tables;
    }


    public SQL2003_V2_Table getSql2003_v2_table() {
        return sql2003_v2_table;
    }

    public void setSql2003_v2_table(SQL2003_V2_Table sql2003_v2_table) {
        this.sql2003_v2_table = sql2003_v2_table;
    }
    public List<SQL2003_V2_Table> getSql2003_v2_tables() {
        return sql2003_v2_tables;
    }

    public void addSql2003_v2_table(Sql2003_v2_table sql2003_v2_table) {
        this.sql2003_v2_tables.add(sql2003_v2_table);
    }

}
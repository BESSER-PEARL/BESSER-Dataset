





import java.util.List;
import java.util.ArrayList;

public class Sql_Column extends NamedElement {

    private String type;





    private Sql_Table sql_table;


    public Sql_Column(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public Sql_Table getSql_table() {
        return sql_table;
    }

    public void setSql_table(Sql_Table sql_table) {
        this.sql_table = sql_table;
    }

}
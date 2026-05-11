





import java.util.List;
import java.util.ArrayList;

public class plSql_Label  {

    private String name;





    private plSql_Statement plsql_statement;


    public plSql_Label(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public plSql_Statement getPlsql_statement() {
        return plsql_statement;
    }

    public void setPlsql_statement(plSql_Statement plsql_statement) {
        this.plsql_statement = plsql_statement;
    }

}
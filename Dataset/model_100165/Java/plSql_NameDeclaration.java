





import java.util.List;
import java.util.ArrayList;

public class plSql_NameDeclaration  {

    private String name;





    private plSql_Name plsql_name;


    public plSql_NameDeclaration(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public plSql_Name getPlsql_name() {
        return plsql_name;
    }

    public void setPlsql_name(plSql_Name plsql_name) {
        this.plsql_name = plsql_name;
    }

}
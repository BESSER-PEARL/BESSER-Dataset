





import java.util.List;
import java.util.ArrayList;

public class Table  {






    private SQLDDL_Parameter sqlddl_parameter;




    private SQLDDL_Database sqlddl_database;




    private SQLDDL_TableElement sqlddl_tableelement;




    private SQLDDL_ForeignKey sqlddl_foreignkey;


    public Table(
    ) {
    }



    public SQLDDL_Parameter getSqlddl_parameter() {
        return sqlddl_parameter;
    }

    public void setSqlddl_parameter(SQLDDL_Parameter sqlddl_parameter) {
        this.sqlddl_parameter = sqlddl_parameter;
    }
    public SQLDDL_Database getSqlddl_database() {
        return sqlddl_database;
    }

    public void setSqlddl_database(SQLDDL_Database sqlddl_database) {
        this.sqlddl_database = sqlddl_database;
    }
    public SQLDDL_TableElement getSqlddl_tableelement() {
        return sqlddl_tableelement;
    }

    public void setSqlddl_tableelement(SQLDDL_TableElement sqlddl_tableelement) {
        this.sqlddl_tableelement = sqlddl_tableelement;
    }
    public SQLDDL_ForeignKey getSqlddl_foreignkey() {
        return sqlddl_foreignkey;
    }

    public void setSqlddl_foreignkey(SQLDDL_ForeignKey sqlddl_foreignkey) {
        this.sqlddl_foreignkey = sqlddl_foreignkey;
    }

}






import java.util.List;
import java.util.ArrayList;

public class Table  {






    private MySQL_Column mysql_column;




    private MySQL_DataBase mysql_database;


    public Table(
    ) {
    }



    public MySQL_Column getMysql_column() {
        return mysql_column;
    }

    public void setMysql_column(MySQL_Column mysql_column) {
        this.mysql_column = mysql_column;
    }
    public MySQL_DataBase getMysql_database() {
        return mysql_database;
    }

    public void setMysql_database(MySQL_DataBase mysql_database) {
        this.mysql_database = mysql_database;
    }

}






import java.util.List;
import java.util.ArrayList;

public class sQL_Column  {

    private String notNull;
    private String dataType;
    private String name;





    private sQL_ForeignKey sql_foreignkey;




    private sQL_ForeignKey sql_foreignkey;




    private sQL_Table sql_table;


    public sQL_Column(
        String notNull,        String dataType,        String name    ) {
        this.notNull = notNull;
        this.dataType = dataType;
        this.name = name;
    }


    public String getNotnull() {
        return notNull;
    }

    public void setNotnull(String notNull) {
        this.notNull = notNull;
    }
    public String getDatatype() {
        return dataType;
    }

    public void setDatatype(String dataType) {
        this.dataType = dataType;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public sQL_ForeignKey getSql_foreignkey() {
        return sql_foreignkey;
    }

    public void setSql_foreignkey(sQL_ForeignKey sql_foreignkey) {
        this.sql_foreignkey = sql_foreignkey;
    }
    public sQL_ForeignKey getSql_foreignkey() {
        return sql_foreignkey;
    }

    public void setSql_foreignkey(sQL_ForeignKey sql_foreignkey) {
        this.sql_foreignkey = sql_foreignkey;
    }
    public sQL_Table getSql_table() {
        return sql_table;
    }

    public void setSql_table(sQL_Table sql_table) {
        this.sql_table = sql_table;
    }

}
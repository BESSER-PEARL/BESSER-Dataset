





import java.util.List;
import java.util.ArrayList;

public class sql_Table extends NamedElement {






    private List<sql_ForeignKey> sql_foreignkeys;




    private sql_PrimaryKey sql_primarykey;




    private sql_ForeignKey sql_foreignkey;




    private sql_PrimaryKey sql_primarykey;




    private List<sql_Column> sql_columns;




    private sql_Schema sql_schema;




    private sql_Column sql_column;




    private List<sql_ForeignKey> sql_foreignkeys;




    private sql_Schema sql_schema;




    private sql_ForeignKey sql_foreignkey;


    public sql_Table(
    ) {
        super(
        );
        this.sql_foreignkeys = new ArrayList<>();
        this.sql_columns = new ArrayList<>();
        this.sql_foreignkeys = new ArrayList<>();
    }

    public sql_Table(
        ArrayList<sql_ForeignKey> sql_foreignkeys,        ArrayList<sql_Column> sql_columns,        ArrayList<sql_ForeignKey> sql_foreignkeys    ) {
        this.sql_foreignkeys = sql_foreignkeys;
        this.sql_columns = sql_columns;
        this.sql_foreignkeys = sql_foreignkeys;
    }


    public List<sql_ForeignKey> getSql_foreignkeys() {
        return sql_foreignkeys;
    }

    public void addSql_foreignkey(Sql_foreignkey sql_foreignkey) {
        this.sql_foreignkeys.add(sql_foreignkey);
    }
    public sql_PrimaryKey getSql_primarykey() {
        return sql_primarykey;
    }

    public void setSql_primarykey(sql_PrimaryKey sql_primarykey) {
        this.sql_primarykey = sql_primarykey;
    }
    public sql_ForeignKey getSql_foreignkey() {
        return sql_foreignkey;
    }

    public void setSql_foreignkey(sql_ForeignKey sql_foreignkey) {
        this.sql_foreignkey = sql_foreignkey;
    }
    public sql_PrimaryKey getSql_primarykey() {
        return sql_primarykey;
    }

    public void setSql_primarykey(sql_PrimaryKey sql_primarykey) {
        this.sql_primarykey = sql_primarykey;
    }
    public List<sql_Column> getSql_columns() {
        return sql_columns;
    }

    public void addSql_column(Sql_column sql_column) {
        this.sql_columns.add(sql_column);
    }
    public sql_Schema getSql_schema() {
        return sql_schema;
    }

    public void setSql_schema(sql_Schema sql_schema) {
        this.sql_schema = sql_schema;
    }
    public sql_Column getSql_column() {
        return sql_column;
    }

    public void setSql_column(sql_Column sql_column) {
        this.sql_column = sql_column;
    }
    public List<sql_ForeignKey> getSql_foreignkeys() {
        return sql_foreignkeys;
    }

    public void addSql_foreignkey(Sql_foreignkey sql_foreignkey) {
        this.sql_foreignkeys.add(sql_foreignkey);
    }
    public sql_Schema getSql_schema() {
        return sql_schema;
    }

    public void setSql_schema(sql_Schema sql_schema) {
        this.sql_schema = sql_schema;
    }
    public sql_ForeignKey getSql_foreignkey() {
        return sql_foreignkey;
    }

    public void setSql_foreignkey(sql_ForeignKey sql_foreignkey) {
        this.sql_foreignkey = sql_foreignkey;
    }

}
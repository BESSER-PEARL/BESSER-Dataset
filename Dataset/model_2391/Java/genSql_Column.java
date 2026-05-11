





import java.util.List;
import java.util.ArrayList;

public class genSql_Column  {

    private String Longitud;
    private String name;
    private String SQLType;





    private genSql_Table gensql_table;




    private genSql_ForeignKey gensql_foreignkey;




    private genSql_PrimaryKey gensql_primarykey;




    private genSql_ForeignKey gensql_foreignkey;


    public genSql_Column(
        String Longitud,        String name,        String SQLType    ) {
        this.Longitud = Longitud;
        this.name = name;
        this.SQLType = SQLType;
    }


    public String getLongitud() {
        return Longitud;
    }

    public void setLongitud(String Longitud) {
        this.Longitud = Longitud;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSqltype() {
        return SQLType;
    }

    public void setSqltype(String SQLType) {
        this.SQLType = SQLType;
    }

    public genSql_Table getGensql_table() {
        return gensql_table;
    }

    public void setGensql_table(genSql_Table gensql_table) {
        this.gensql_table = gensql_table;
    }
    public genSql_ForeignKey getGensql_foreignkey() {
        return gensql_foreignkey;
    }

    public void setGensql_foreignkey(genSql_ForeignKey gensql_foreignkey) {
        this.gensql_foreignkey = gensql_foreignkey;
    }
    public genSql_PrimaryKey getGensql_primarykey() {
        return gensql_primarykey;
    }

    public void setGensql_primarykey(genSql_PrimaryKey gensql_primarykey) {
        this.gensql_primarykey = gensql_primarykey;
    }
    public genSql_ForeignKey getGensql_foreignkey() {
        return gensql_foreignkey;
    }

    public void setGensql_foreignkey(genSql_ForeignKey gensql_foreignkey) {
        this.gensql_foreignkey = gensql_foreignkey;
    }

}
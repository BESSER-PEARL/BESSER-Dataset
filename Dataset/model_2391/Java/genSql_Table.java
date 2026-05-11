





import java.util.List;
import java.util.ArrayList;

public class genSql_Table  {

    private String name;





    private List<genSql_ForeignKey> gensql_foreignkeys;




    private genSql_ForeignKey gensql_foreignkey;




    private genSql_PrimaryKey gensql_primarykey;




    private genSql_DataBase gensql_database;


    public genSql_Table(
        String name    ) {
        this.name = name;
        this.gensql_foreignkeys = new ArrayList<>();
    }

    public genSql_Table(
        String name        ArrayList<genSql_ForeignKey> gensql_foreignkeys    ) {
        this.name = name;
        this.gensql_foreignkeys = gensql_foreignkeys;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<genSql_ForeignKey> getGensql_foreignkeys() {
        return gensql_foreignkeys;
    }

    public void addGensql_foreignkey(Gensql_foreignkey gensql_foreignkey) {
        this.gensql_foreignkeys.add(gensql_foreignkey);
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
    public genSql_DataBase getGensql_database() {
        return gensql_database;
    }

    public void setGensql_database(genSql_DataBase gensql_database) {
        this.gensql_database = gensql_database;
    }

}






import java.util.List;
import java.util.ArrayList;

public class database_Column  {

    private boolean IsPrimaryKey;
    private String Name;
    private String Type;





    private database_ForeignKey database_foreignkey;




    private database_ForeignKey database_foreignkey;




    private database_Table database_table;




    private database_Table database_table;


    public database_Column(
        boolean IsPrimaryKey,        String Name,        String Type    ) {
        this.IsPrimaryKey = IsPrimaryKey;
        this.Name = Name;
        this.Type = Type;
    }


    public boolean getIsprimarykey() {
        return IsPrimaryKey;
    }

    public void setIsprimarykey(boolean IsPrimaryKey) {
        this.IsPrimaryKey = IsPrimaryKey;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }

    public database_ForeignKey getDatabase_foreignkey() {
        return database_foreignkey;
    }

    public void setDatabase_foreignkey(database_ForeignKey database_foreignkey) {
        this.database_foreignkey = database_foreignkey;
    }
    public database_ForeignKey getDatabase_foreignkey() {
        return database_foreignkey;
    }

    public void setDatabase_foreignkey(database_ForeignKey database_foreignkey) {
        this.database_foreignkey = database_foreignkey;
    }
    public database_Table getDatabase_table() {
        return database_table;
    }

    public void setDatabase_table(database_Table database_table) {
        this.database_table = database_table;
    }
    public database_Table getDatabase_table() {
        return database_table;
    }

    public void setDatabase_table(database_Table database_table) {
        this.database_table = database_table;
    }

}






import java.util.List;
import java.util.ArrayList;

public class database_Column  {

    private boolean PrimaryKey;
    private String type;
    private String name;
    private boolean NotNull;





    private database_Table database_table;




    private database_Scheme database_scheme;




    private database_Table database_table;




    private database_Column database_column;


    public database_Column(
        boolean PrimaryKey,        String type,        String name,        boolean NotNull    ) {
        this.PrimaryKey = PrimaryKey;
        this.type = type;
        this.name = name;
        this.NotNull = NotNull;
    }


    public boolean getPrimarykey() {
        return PrimaryKey;
    }

    public void setPrimarykey(boolean PrimaryKey) {
        this.PrimaryKey = PrimaryKey;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getNotnull() {
        return NotNull;
    }

    public void setNotnull(boolean NotNull) {
        this.NotNull = NotNull;
    }

    public database_Table getDatabase_table() {
        return database_table;
    }

    public void setDatabase_table(database_Table database_table) {
        this.database_table = database_table;
    }
    public database_Scheme getDatabase_scheme() {
        return database_scheme;
    }

    public void setDatabase_scheme(database_Scheme database_scheme) {
        this.database_scheme = database_scheme;
    }
    public database_Table getDatabase_table() {
        return database_table;
    }

    public void setDatabase_table(database_Table database_table) {
        this.database_table = database_table;
    }
    public database_Column getDatabase_column() {
        return database_column;
    }

    public void setDatabase_column(database_Column database_column) {
        this.database_column = database_column;
    }

}
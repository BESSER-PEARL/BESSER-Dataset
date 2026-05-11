





import java.util.List;
import java.util.ArrayList;

public class database_Column extends RefColumn {

    private String name;





    private database_FKey database_fkey;


    public database_Column(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public database_FKey getDatabase_fkey() {
        return database_fkey;
    }

    public void setDatabase_fkey(database_FKey database_fkey) {
        this.database_fkey = database_fkey;
    }

}
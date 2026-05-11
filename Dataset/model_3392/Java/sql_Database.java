





import java.util.List;
import java.util.ArrayList;

public class sql_Database  {

    private String name;
    private String TypeDB;



    public sql_Database(
        String name,        String TypeDB    ) {
        this.name = name;
        this.TypeDB = TypeDB;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTypedb() {
        return TypeDB;
    }

    public void setTypedb(String TypeDB) {
        this.TypeDB = TypeDB;
    }


}
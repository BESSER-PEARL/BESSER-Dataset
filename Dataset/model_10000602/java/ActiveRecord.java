





import java.util.List;
import java.util.ArrayList;

public class ActiveRecord  {

    private int id;
    private None connection;



    public ActiveRecord(
        int id,        None connection    ) {
        this.id = id;
        this.connection = connection;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public None getConnection() {
        return connection;
    }

    public void setConnection(None connection) {
        this.connection = connection;
    }


}
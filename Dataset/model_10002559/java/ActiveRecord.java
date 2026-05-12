





import java.util.List;
import java.util.ArrayList;

public class ActiveRecord  {

    private None connection;
    private int id;



    public ActiveRecord(
        None connection,        int id    ) {
        this.connection = connection;
        this.id = id;
    }


    public None getConnection() {
        return connection;
    }

    public void setConnection(None connection) {
        this.connection = connection;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }


}
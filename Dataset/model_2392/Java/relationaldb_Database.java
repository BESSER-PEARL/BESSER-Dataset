





import java.util.List;
import java.util.ArrayList;

public class relationaldb_Database extends Named {

    private String rawDatabase;



    public relationaldb_Database(
        String rawDatabase    ) {
        super(
        );
        this.rawDatabase = rawDatabase;
    }


    public String getRawdatabase() {
        return rawDatabase;
    }

    public void setRawdatabase(String rawDatabase) {
        this.rawDatabase = rawDatabase;
    }


}
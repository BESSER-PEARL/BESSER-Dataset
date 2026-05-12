





import java.util.List;
import java.util.ArrayList;

public class plSql_PragmaTimestamp extends Pragma {

    private String timestamp;



    public plSql_PragmaTimestamp(
        String timestamp    ) {
        super(
        );
        this.timestamp = timestamp;
    }


    public String getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(String timestamp) {
        this.timestamp = timestamp;
    }


}






import java.util.List;
import java.util.ArrayList;

public class oracle_OracleTableProperty  {

    private String tabletype;
    private String space;



    public oracle_OracleTableProperty(
        String tabletype,        String space    ) {
        this.tabletype = tabletype;
        this.space = space;
    }


    public String getTabletype() {
        return tabletype;
    }

    public void setTabletype(String tabletype) {
        this.tabletype = tabletype;
    }
    public String getSpace() {
        return space;
    }

    public void setSpace(String space) {
        this.space = space;
    }


}
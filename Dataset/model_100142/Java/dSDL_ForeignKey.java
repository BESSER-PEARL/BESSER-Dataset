





import java.util.List;
import java.util.ArrayList;

public class dSDL_ForeignKey extends Property {

    private String tableName;
    private String attributeName;



    public dSDL_ForeignKey(
        String tableName,        String attributeName    ) {
        super(
        );
        this.tableName = tableName;
        this.attributeName = attributeName;
    }


    public String getTablename() {
        return tableName;
    }

    public void setTablename(String tableName) {
        this.tableName = tableName;
    }
    public String getAttributename() {
        return attributeName;
    }

    public void setAttributename(String attributeName) {
        this.attributeName = attributeName;
    }


}
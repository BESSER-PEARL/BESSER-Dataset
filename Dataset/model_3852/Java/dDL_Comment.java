





import java.util.List;
import java.util.ArrayList;

public class dDL_Comment extends Definition {

    private String string;
    private String columnId;



    public dDL_Comment(
        String string,        String columnId    ) {
        super(
        );
        this.string = string;
        this.columnId = columnId;
    }


    public String getString() {
        return string;
    }

    public void setString(String string) {
        this.string = string;
    }
    public String getColumnid() {
        return columnId;
    }

    public void setColumnid(String columnId) {
        this.columnId = columnId;
    }


}
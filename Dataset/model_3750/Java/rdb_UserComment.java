





import java.util.List;
import java.util.ArrayList;

public class rdb_UserComment  {

    private String comment;





    private rdb_Table rdb_table;


    public rdb_UserComment(
        String comment    ) {
        this.comment = comment;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    public rdb_Table getRdb_table() {
        return rdb_table;
    }

    public void setRdb_table(rdb_Table rdb_table) {
        this.rdb_table = rdb_table;
    }

}
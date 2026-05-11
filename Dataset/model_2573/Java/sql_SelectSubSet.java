





import java.util.List;
import java.util.ArrayList;

public class sql_SelectSubSet  {

    private String all;
    private String op;



    public sql_SelectSubSet(
        String all,        String op    ) {
        this.all = all;
        this.op = op;
    }


    public String getAll() {
        return all;
    }

    public void setAll(String all) {
        this.all = all;
    }
    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }


}
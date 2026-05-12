





import java.util.List;
import java.util.ArrayList;

public class sql_SelectSubSet  {

    private String op;
    private String all;



    public sql_SelectSubSet(
        String op,        String all    ) {
        this.op = op;
        this.all = all;
    }


    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }
    public String getAll() {
        return all;
    }

    public void setAll(String all) {
        this.all = all;
    }


}
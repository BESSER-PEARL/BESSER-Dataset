





import java.util.List;
import java.util.ArrayList;

public class mt_core_ASTNode  {

    private int end;
    private int begin;



    public mt_core_ASTNode(
        int end,        int begin    ) {
        this.end = end;
        this.begin = begin;
    }


    public int getEnd() {
        return end;
    }

    public void setEnd(int end) {
        this.end = end;
    }
    public int getBegin() {
        return begin;
    }

    public void setBegin(int begin) {
        this.begin = begin;
    }


}
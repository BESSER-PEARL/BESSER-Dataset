





import java.util.List;
import java.util.ArrayList;

public class express_RepeatStatement extends Statement {

    private String end;
    private String idx;
    private String start;



    public express_RepeatStatement(
        String end,        String idx,        String start    ) {
        super(
        );
        this.end = end;
        this.idx = idx;
        this.start = start;
    }


    public String getEnd() {
        return end;
    }

    public void setEnd(String end) {
        this.end = end;
    }
    public String getIdx() {
        return idx;
    }

    public void setIdx(String idx) {
        this.idx = idx;
    }
    public String getStart() {
        return start;
    }

    public void setStart(String start) {
        this.start = start;
    }


}
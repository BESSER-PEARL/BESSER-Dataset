





import java.util.List;
import java.util.ArrayList;

public class shr5Management_RangeTableEntry  {

    private int from_;
    private int to;



    public shr5Management_RangeTableEntry(
        int from_,        int to    ) {
        this.from_ = from_;
        this.to = to;
    }


    public int getFrom_() {
        return from_;
    }

    public void setFrom_(int from_) {
        this.from_ = from_;
    }
    public int getTo() {
        return to;
    }

    public void setTo(int to) {
        this.to = to;
    }


}
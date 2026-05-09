





import java.util.List;
import java.util.ArrayList;

public class reviews_LineRange  {

    private int start;
    private int end;





    private reviews_LineLocation reviews_linelocation;


    public reviews_LineRange(
        int start,        int end    ) {
        this.start = start;
        this.end = end;
    }


    public int getStart() {
        return start;
    }

    public void setStart(int start) {
        this.start = start;
    }
    public int getEnd() {
        return end;
    }

    public void setEnd(int end) {
        this.end = end;
    }

    public reviews_LineLocation getReviews_linelocation() {
        return reviews_linelocation;
    }

    public void setReviews_linelocation(reviews_LineLocation reviews_linelocation) {
        this.reviews_linelocation = reviews_linelocation;
    }

}
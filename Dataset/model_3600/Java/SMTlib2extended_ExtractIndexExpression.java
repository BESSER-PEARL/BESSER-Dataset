





import java.util.List;
import java.util.ArrayList;

public class SMTlib2extended_ExtractIndexExpression extends UnaryExpression {

    private int end;
    private int start;



    public SMTlib2extended_ExtractIndexExpression(
        int end,        int start    ) {
        super(
        );
        this.end = end;
        this.start = start;
    }


    public int getEnd() {
        return end;
    }

    public void setEnd(int end) {
        this.end = end;
    }
    public int getStart() {
        return start;
    }

    public void setStart(int start) {
        this.start = start;
    }


}